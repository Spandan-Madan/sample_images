import os 

with open('index_template.html','r') as F:
    content = F.readlines()
    
lines = []

image_paths = [i for i in os.listdir('./images') if '.jpg' in i]
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

