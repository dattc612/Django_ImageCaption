from torch.types import Device
from torchvision import transforms
import torch
from torch import nn
import pickle
from torch.nn import functional as F
import os
from django.conf import settings

class Decoder(nn.Module):
	"""
	  encoderImage_size: kích thước ảnh encode
	  input_size: kích thước vocab
	  hidden_size: kích thước lớp ẩn 
	    
	"""
	def __init__(self,encoderImage_size, input_size, hidden_size):
		
	  super(Decoder,self).__init__()
	  
	  self.hidden_size = hidden_size

	  self.encoderImage_size = encoderImage_size
	  self.linear = nn.Linear(encoderImage_size, hidden_size)

	  self.embedding = nn.Embedding(input_size,hidden_size)
	  self.gru = nn.GRU( hidden_size, hidden_size)
	  self.out = nn.Linear(hidden_size, input_size)
	
	def forward(self, input, hidden):

		embedded = self.embedding(input).view(1,1,-1)
		output = F.relu(embedded)
		output, hidden = self.gru(output, hidden)
		output = self.out(output[0])
		return output, hidden

	def initHidden(self, input):
		return self.linear(input).reshape(1, 1, -1)


TRANSFROM = transforms.Compose([ 
                                 transforms.ToTensor(),
                                 transforms.Resize((300,300))
])

DATA_FOR_DEEP = settings.DATA_FOR_DEEP

SOS_token = 1

DEVICE = torch.device('cpu')

with open(os.path.join(DATA_FOR_DEEP,'vocab.txt'),'rb') as f:
  VOCAB = pickle.load(f)


ENCODER = torch.load(os.path.join(DATA_FOR_DEEP,'encoder2.pth'), map_location=DEVICE)


DECODER = Decoder(2048, len(VOCAB), 256)
DECODER.load_state_dict(torch.load(os.path.join(DATA_FOR_DEEP, 'decoder.pth'), map_location=DEVICE))
#DECODER.to(DEVICE)

##################################################################################



def search(image):

	lst_word = []
	image = TRANSFROM(image)
	image =  ENCODER(image.unsqueeze(0))

	decoder_hidden = DECODER.initHidden(image)
	decoder_input = torch.tensor([[SOS_token]], device=DEVICE )

	out = torch.argmax(decoder_input)


	while (out.item()!=1) and (len(lst_word)<15):
		decoder_output, decoder_hidden = DECODER(decoder_input, decoder_hidden)
		out = torch.argmax(decoder_output)
		decoder_input = out
		lst_word.append(VOCAB[out.item()])
	return ' '.join(lst_word[:-1]).replace('_', ' ')



