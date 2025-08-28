import os 
import glob 

img_paths = glob.glob('*.jpg')
new_paths = []
def  padding(n):
    n_str = str(n)
    while  len(n_str) != 4:
        n_str= "0" + n_str

    return  n_str

for i, img_path in enumerate(img_paths):
    new_path=  img_path.split('_')[1:]
    padding_zeros = padding(i)
    file_ending = '.'+new_path[1].split('.')[-1]
    fp_new_path = new_path[0][2:] +'_IMG_'+ padding_zeros+ f'{file_ending}'
    # new_paths.append(fp_new_path)
    os.rename(img_paths[i],fp_new_path)


    
    