from pydub import AudioSegment
import os

path = os.path.realpath(os.path.dirname(__file__))
inputPath = path+"/input/"
outputPath = path+"/output/"
chunkPath = path+"/chunks/"
keyword = open(path+"/keyword.txt").readline().strip()

os.system("rm -rf "+outputPath+"*")
os.system("rm -rf "+chunkPath+"*")

chunkLength = 5115 #5.115 seconds

counter = 1
for i in os.listdir(inputPath):
    f = os.path.join(inputPath, i)
    if f.endswith(".wav"):
        original = AudioSegment.from_wav(f)
        duration = round(original.duration_seconds*1000)
        for x, j in enumerate(range(chunkLength,duration,chunkLength)):
            chunkName = "{}{} ({}).wav".format(chunkPath, keyword, counter)
            specName = "{}{} ({}).png".format(outputPath, keyword, counter)
            chunk = original[j-chunkLength:j].export(chunkName, format="wav")
            os.system("python -m riffusion.cli audio-to-image -a \"{}\" -i \"{}\"".format(chunkName, specName))
            print("\n\n[*] Completed chunk "+str(counter)+"\n\n")
            counter += 1
