# **Retake Readme File**

***
## Personal Thoughts
Due to my lack of understanding and ability in some areas of code, I was unable to meet all the criteria for my original project. Looking back at this I can fully understand why this was the case, and I have done my very best to take the assessors constructive critisim onboard, and have gone back at this project with a renewed look and vision, and have rectified my failings.
***
# Content

- **[Failings](#failings)**
    - [Fail One](#fail-one)
    - [Fail Two](#fail-two)
    - [Fail Three](#fail-three)
- **[Fixes](#fixes)**
    - [Fix One](#fix-one)
    - [Fix Two](#fix-two)
    - [Fix Three](#fix-three)
- **[Errors](#errors)**
    - [W3C](#w3c)
- **[Future Implications](#future-implications)**
- **[Final Comments](#final-comments)**

## **Failings**
***
### Fail One
![Fail One](readme-content/retake/10.%20Fail%20One%20-%20Assessor.png)

### Fail Two
![Fail Two](readme-content/retake/11.%20Fail%20Two%20-%20Assessor.png)

### Fail Three
![Fail Three](readme-content/retake/12.%20Fail%20Three%20-%20Assessor.png)

## **Fixes**
***
### **Fix One**
***
In order to try and remove the red underline in this code, as it was throwing an error ('line too long') within my code, I used the '\' function to cut the lines in half. Due to this '\' it caused my sign in and sign up functions to fail from the get go. This was an oversight on my part, and will be an error I will not be making in the future. I would rather have a few squiggly red underlines within my code, than app breaking code but clean, error free code.

![Fix One](readme-content/retake/10.%20Fail%20One%20-%20Reason.png)


### **Fix Two**
***
This fix was less simple, and required me to take a long hard look at the user experience within the app. I orginally thought that I would be able to go through the admin page to create 'blogs' or 'posts' for my users, but this was clearly a huge oversight on my part, and I'm not quite sure what I was thinking. I'm going to put the blame on a very bad week at work for that decision! However, with this in mind, I tackled the issue head on and created the code that would allow users to create their own posts, edit them and then delete them. I have also allowed them the ability to view all their own posts on their own individual profile.

Below are screen shots of the new content that has been implimented into the application.

### New Nav Bar
![New Nav Bar](readme-content/retake/1.%20New%20Nav%20Bar.png)

### Add Post
![Add Post](readme-content/retake/2.%20Add%20Post.png)

### Posts
![Posts](readme-content/retake/3.%20Posts.png)

### Individual Posts
![Individual Posts](readme-content/retake/4.%20Individual%20Post.png)

### Edit Posts
![Edit Post](readme-content/retake/5.%20Edit%20Post.png)

### Delete Posts
![Delete Post](readme-content/retake/6.%20Delete%20Post.png)

### Profile
![Profile](readme-content/retake/7.%20Profile.png)

### Edit Email
![Edit Email](readme-content/retake/8.%20Edit%20Email.png)

### Edit Password
![Edit Password](readme-content/retake/9.%20Edit%20Password.png)

### **Fix Three**

***

After talking to my mentor *Martina*, we came to the conclusion that this error must have been in relation to the first error upon which the examiner was not even able to access the site due to the error within the settings.py file. Due to this now being fixed, and a profile section being set up for people to join the site, this error is fixed. 

I do have Martina's permission to mention her within my *'fix'* section, as proof we have tried to recreate the error to try and fix it, only to find out the error did not exist for us. As mentioned above, I believe that to be the reason why.

## **Errors**

***
CSS was not loading on the Live website, however it was applying itself when in the gitpod runserver command.

![CSS](readme-content/retake/01%20-%20CSS%20not%20applying.png)
![CSS Not Applying](readme-content/retake/02%20-%20CSS%20not%20applying%2C%20but%20works%20in%20github.png)
![CSS MIME](readme-content/retake/03%20-%20CSS%20not%20applying%2C%20MIME.png)

The fix for this was that debug was set to True in settings. Which would have been an automatic fail! However that is now set to False and everything works perfectly fine.

Heroku was failing to load the site.
![Heroku Fail](readme-content/retake/04%20-%20Heroku%20Failing%20To%20Load.png)
A simple fix for this was to comment out the debug setting, after talking to a tutor, I believe this is something to do with django having it's own set of debugging tools when in production. If there is a more effecient way to fix this, I hope to find it for future projects.

### **W3C**

This first screenshot applied for the majority of the website, so instead of having multiple screenshots, I have left only this one in.
![Validator](readme-content/retake/05.%20Validator.png)

This is the profile validator;
![Validator](readme-content/retake/06.%20Validator%20Profile.png)

This is the post validator;
![Validator](readme-content/retake/07.%20Validator%20Post.png)

This is the update validator;
![Validator](readme-content/retake/08.%20Validator%20Update.png)

This is the delete validator;
![Validator](readme-content/retake/09.%20Validator%20Delete.png)

It may be my lack of understanding, but after going through the templates within my code, to fix these errors, I noticed that where the majority read 'error' the line number associated with it was incorrect. For example on the 'post validator' screenshot is shows 'stray end tag', however when looking at my code within the post.html file, it shows that the '</ header>' is part of the correct section of code. As mentioned, this might be an oversight of my understanding, but I thought it best to make note of this.

## **Future Implications**

***
If I had been given longer to retake this Project (ideally if I had completed it correctly to begin with) I would have liked to impliment some of the following;
    
- likes and comments; as found in the blog section
- the ability to click on someones comment to take you to their profile page
    - though I like to think this would be as simple as adding an < a > to the blog_details page by the 'comment.name', it is something I'd like to look into properly.
- I would like the ability to allow users to access their drafts so they can edit and post them when they are ready too, rather than relying on the admin to post it for them.
- I am unhappy with the size of the photos when a user clicks on the post, as it takes up the entire screen, unfortunately I am quickly running out of time to redo this project due to work commitments, but I am acknowledging that it does not look the best, and I would like to fix this given time.
- I would also like to fix an issue where users are unable to do paragraphs in their posts. I am not sure why this is, I believe it is something to do with the crispy forms. But I could be wrong.

## **Final Comments**

I understand that this resubmission is a little rough around the edges. I do believe that given more time, I would have been able to polish it off quite nicely. However with only 10 days allowed for resubmission, along with work commitments and an unfortunate leave of absence, I found this quite difficult, especially after not looking at the code for quite some time due to working on Project 5. I do believe though that I understand a lot more of why somethings behave the way they do, having done project five and then having to come back to this project.

Thank you for taking the time to read this resubmission README.md file. I wish to thank my new Mentor Martina as well, as mentioned above for her extensive knowledge, and reassuring me about the future in the field of coding.