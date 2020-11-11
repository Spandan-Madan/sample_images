import os 
import shutil


data_folder = "/home/smadan/data_differentiable_interpretability/rendered_train_data/jpgs"
server_folder = "/home/smadan/sample_images/images/"


print("Removing existing files....")
for im in os.listdir(server_folder):
    os.remove("%s/%s"%(server_folder, im))

print("Copying new files....")
for im in os.listdir(data_folder):
    shutil.copyfile("%s/%s"%(data_folder, im), "%s/%s"%(server_folder, im))

print("building template....")
with open('index_template.html','r') as F:
    content = F.readlines()
    
lines = []


image_paths = ["images/%s"%i for i in os.listdir('./images') if '.jpg' in i]
num_columns = 4
num_rows = int(len(image_paths)/num_columns)

for c in content:
    if "Photo Grid" in c:
        lines.append('<div>\n')
        lines.append('<div class="row">\n')
        for col_num in range(num_columns):
            lines.append('<div class="column">\n')
            for row_num in range(num_rows):
                im_path = image_paths[row_num*num_columns + col_num]
                im_string = '<img src="%s" '%im_path + 'style="width:100%">\n'
                lines.append(im_string)
            lines.append('</div>\n')
        lines.append('</div>\n')
    else:
        lines.append(c)

with open('index.html','w') as F:
    F.writelines(lines)

print('Updating on git')
os.system('git add -A')
os.system('git commit -m "adding new images"')
os.system('git push')
print("Completed, please visit - http://spandan-madan.github.io/sample_images/")
# <div>        
#   <div class="column">
#     <img src="../w3images/underwater.jpg" style="width:100%">
#     <img src="../w3images/ocean.jpg" style="width:100%">
#     <img src="../w3images/wedding.jpg" style="width:100%">
#     <img src="../w3images/mountainskies.jpg" style="width:100%">
#     <img src="../w3images/rocks.jpg" style="width:100%">
#     <img src="../w3images/underwater.jpg" style="width:100%">
#   </div>
#   <div class="column">
#     <img src="../w3images/underwater.jpg" style="width:100%">
#     <img src="../w3images/ocean.jpg" style="width:100%">
#     <img src="../w3images/wedding.jpg" style="width:100%">
#     <img src="../w3images/mountainskies.jpg" style="width:100%">
#     <img src="../w3images/rocks.jpg" style="width:100%">
#     <img src="../w3images/underwater.jpg" style="width:100%">
#   </div>
#   <div class="column">
#     <img src="../w3images/wedding.jpg" style="width:100%">
#     <img src="../w3images/rocks.jpg" style="width:100%">
#     <img src="../w3images/falls2.jpg" style="width:100%">
#     <img src="../w3images/paris.jpg" style="width:100%">
#     <img src="../w3images/nature.jpg" style="width:100%">
#     <img src="../w3images/mist.jpg" style="width:100%">
#     <img src="../w3images/paris.jpg" style="width:100%">
#   </div>
#   <div class="column">
#     <img src="../w3images/underwater.jpg" style="width:100%">
#     <img src="../w3images/ocean.jpg" style="width:100%">
#     <img src="../w3images/wedding.jpg" style="width:100%">
#     <img src="../w3images/mountainskies.jpg" style="width:100%">
#     <img src="../w3images/rocks.jpg" style="width:100%">
#     <img src="../w3images/underwater.jpg" style="width:100%">
#   </div>
# </div>

