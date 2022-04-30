import wave

pink_noise_file_name = "PinkNoise.wav"

infiles = []
outfile = "FullPinkNoise.wav"

silence_minutes = 60
pink_noise_minutes = 600

for i in range(pink_noise_minutes*2):
    infiles.append(pink_noise_file_name)

data= []
for infile in infiles:
    w = wave.open(infile, 'rb')
    data.append( [w.getparams(), w.readframes(w.getnframes())] )
    w.close()

output = wave.open(outfile, 'wb')
output.setparams(data[0][0])
for i in range(silence_minutes*2):
    output.writeframes(bytearray(len(data[0][1])))
    print(i)
for i in range(len(data)):
    print(i)
    output.writeframes(data[i][1])
output.close()
