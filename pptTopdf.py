import comtypes.client
import os

def init_powerpoint():
	powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
	powerpoint.Visible = 1
	return powerpoint

def ppt_to_pdf(powerpoint,inputFileName,outFileName,formatType = 32):
	if outFileName[-3:]!='pdf':
		if(outFileName.endswith('.ppt')):
			outFileName = outFileName[0:-4]
		if(outFileName.endswith('.pptx')):
			outFileName = outFileName[0:-5]
		outFileName = outFileName + '.pdf'
		print(outFileName)
	deck = powerpoint.Presentations.Open(inputFileName)
	deck.SaveAs(outFileName,formatType)
	deck.close
	
def convert_files_in_folder(powerpoint,folder):
	files = os.listdir(folder)
	pptfiles = [f for f in files if f.endswith((".ppt",".pptx"))]
	
	for pptfile in pptfiles:
		fullpath = os.path.join(cwd,pptfile)
		ppt_to_pdf(powerpoint,fullpath,fullpath)
		
if __name__ == '__main__':
	powerpoint = init_powerpoint()
	cwd = os.getcwd()
	convert_files_in_folder(powerpoint,cwd)
	powerpoint.Quit()