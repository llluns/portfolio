#Phantom script: 




i=len(projects)


#for range(i):
#    format the stuff we want 

for project in projects:
    h3= project[title] 
    h4=project[location]
    h5=project[class]
    h6=project[date]
    p=project[description]


////////////////////////////////

## GET ALL INSTAGRAM PHOTOS - Python

#Retrieve using the API
#Put into folder




## GRAB ALL IG PHOTOS FROM FILE AND FORMAT - JS


#figuring out how many pics we need in each column
num_pics=len(files in folder)
pics_per_col=num_pics/3
if remainder(num_pics/3)==0:
    num_col_1=pics_per_col
    num_col_2=pics_per_col
    num_col_3=pics_per_col
elif remainder(num_pics/3)==1:
    num_col_1=pics_per_col +1
    num_col_2=pics_per_col
    num_col_3=pics_per_col
elif remainder(num_pics/3)==1:
    num_col_1=pics_per_col +1
    num_col_2=pics_per_col+1
    num_col_3=pics_per_col

#creating empty list to put photo information into
col_1_pics=[]
col_2_pics=[]
col_3_pics=[]

#Sorting images into columns such that the newest photos are higher on the column

for index in range(num_pics):
    if remainder(index/3)==1:
        col_1_pics.append(pics[index])
    elif remainder (index/3)==2:
        col_2_pics.append(pics[index])
    else:
        col_3_pics.append(pics[index])
    index+=1

