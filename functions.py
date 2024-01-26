def listCourses(courses): 
    print("Courses:")
    counter = 1
    for cur in courses:
        data="{0}. Code: {1} | Name: {2} ({3} Credits)"
        print(data.format(counter, cur[0], cur[1], cur[2]))
        counter=counter+1
    print("")