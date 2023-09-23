## CONTENTS

* [Introduction](#introduction-digital-patient)
* [User Experience - UX](#user-experience)
  * [UX](#ux)
    * [Site purpose](#site-purpose)
    * [Site goal](#site-goal)
    * [Audience](#audience)
  * [User stories](#user-stories)
    * [First time user goals](#first-time-user-goals)
    * [Returning user goals](#returning-user-goals)
  * [Agile methodology](#agile-methodology)
  * [Design](#design)
    * [Colours](#colours)
    * [Typography](#typography)
    * [Media](#media)
    * [Database schema](#database-schema)
    * [Wireframes](#wireframes)
* [Features](#features)
  * [Existing features](#existing-features)
  * [Future features](#future-features)
* [Technologies used](#technologies-used)
  * [Languages](#languages)
  * [Frameworks libraries, programs](#frameworks-libraries-programs)
* [Testing](TESTING.md)
* [Deployment](#deployment)
  * [Forking](#forking)
  * [Cloning the repo with GitPod or Codeanywhere](#cloning-the-repo-with-gitpod-or-codeanywhere)
  * [Running the project locally](#running-the-project-locally)
  * [Deploying with Heroku](#deploying-with-heroku)
* [Credits](#credits)


# Introduction: Digital patient

Project Portfolio 4 for Code Institute Full-stack development program. Digital patient is a full stack Django project that runs on Heroku.

The site allows users to register and log in from the frontend. Once registered and logged in users can edit personal data, edit, add and delete diseases/medications, doctors and contacts.

The live website on Heroku can be accessed at the following link: [View my Live Website here](https://digital-patient-807175a8312b.herokuapp.com/)


![Digital patient](static/media/readme/mockup.JPG)

# User Experience
<a href="#top">Back to the top.</a>

## UX

### Site purpose

This program is designed to make it easier for a patient to keep track of their doctors, diseases, medications, as well as (emergency) contacts. In addition, in the case of an emergency, it should be possible for doctors to see a readable version of the patient's profile to see previous diseases, medications, previous doctors and emergency contacts.

### Site goal

To build a website where a kind of digital patient dossier can be easily shared by the patient him/herself for possible emergencies.

A tool like this does not (yet) exist in Germany, and in the case of an emergency with, for example, an unconscious patient, the doctors may not know any previous diseases, medications, general practitioners or emergency contacts, or they may first have to laboriously collect these on individual platforms or (mobile) devices.

### Audience

For anyone who wants to have all their emergency data on one platform for potential doctors in case of an emergency.

## User stories

### First time user goals

- As a first time user I can find information what the purpose of the website is.

### Returning user goals

- As a (returning) user I can register for an account so that I can login after registration.
- As a returning user I can log in to my registered account.
- As a returning user I can log out of my registered account.
- As a returning user I can edit my personal data.
- As a returning user I can edit, add and delete medication/diseases, doctors and contacts in my registered account.
- As a returning user I can share a readable version of my account with potential doctors in case of an emergency.

## Agile methodology

The principles of agile methodology were utilized during the project. Github issues were used to create User Stories for the project. Each user story (including user acceptance criteria, tasks and story points) can be displayed on the board or in the issues. By assigning user stories to issues and taking advantage of the GitHub Kanban board functionality, the necessary goals and priorities throughout the project could be well defined. In addition, labels were used to further define the priority of each user story in the Kanban board.

Through the use of the Kanban board in the projects view in Github, the project was divived into a few different sections:

- Add-ons
- To-do
- In progress
- Done

Milestones were used to create sprints. There were 3 sprints each dated appropriately. User Stories were completed based on the current sprint in progress. Each sprint was completed on time.

## Design

### Colors

I decided to use calming colors, primarily shades of blue. Blue is the typical business color, as it is sober, businesslike, calming and trustworthy, and it maintains its character even in different gradations. It best connects to the goal of the website. To keep the contrast between the background and the font, a basis black tone and a lightly grey is included. All colors also connect to Bootstrap's existing colors (primary, secondary and dark).

![Colors](static/media/readme/color-scheme-digital-patient.JPG)

### Typography

Utilized the Bootstrap 5 native font stack that selects the best font-family for each OS and device. Besides this, the font gives a calm and serious impression.

### Media
The pictures (background image, favicons) were taken from [Pixabay](https://pixabay.com/).

### Database scheme
The database model reflects the different areas of the website: the personal data through the model "UserProfile", the entries for medications/diseases through the model "MediDisLis", the entries for doctors through the model "Doctor" and the entries for contacts through the model "Contact".

![Database scheme](static/media/readme/database-schema.png)

### Wireframes
Initial wireframes

#### Home page

![Home page](static/media/readme/wireframe-home.png)

#### Register

![Register](static/media/readme/wireframe-register.png)

#### Login

![Login](static/media/readme/wireframe-login.png)

#### Overview (profile)

![Overview](static/media/readme/wireframe-profile-overview.png)

#### Personal data

![Personal data](static/media/readme/wireframe-personal-data-view.png)

#### Edit personal data

![Edit personal data](static/media/readme/wireframe-edit-personal-data.png)

#### Medications/Diseases

![Medications/Diseases](static/media/readme/wireframes-medications-diseases.png)

#### Doctors

![Doctors](static/media/readme/wireframe-doctors.png)

#### Contacts

![Contacts](static/media/readme/wireframe-contacts.png)

# Features
<a href="#top">Back to the top.</a>

## Existing features

- __Home screen__
  - The home screen shows information about the website and explains briefly in a FAQ the most important things.
  - The image is intended to symbolize the interface between doctor and patient via the digital medium/the website.

  ![Home screen](static/media/readme/home-screen.png)

- __Navigation Bar__
  - The navigation bar appears on each page.
  - The home screen can be displayed by clicking on the logo on the left side.
  - The navigation bar for unauthenticated users contains links to the home screen, register and login.

  ![Navigation bar unauthenticated users](static/media/readme/navigation-bar-unauthenticated.png)

  - The navigation bar for authenticated users contains links for logout and a drop down menu with links to the five important pages of the website: Overview (profile), personal data, medication/diseases, doctors, contacts.

  ![Navigation bar authenticated users](static/media/readme/navigation-bar-authenticated.png)
  ![Navigation bar authenticated users dropdown](static/media/readme/navigation-bar-authenticated-drop-down.png)

  - The navigation bar will allow the users to easily navigate from page to page across all devices.
  - The navigation bar is fully responsive. On smaller devices, the hamburger menu appears with an expanded menu bar.

  ![Navigation bar unauthenticated users mobile](static/media/readme/navigation-bar-unauthenticated-mobile.png)

  ![Navigation bar authenticated users mobile](static/media/readme/navigation-bar-authenticated-mobile.png)

- __Footer__
  - The footer appears on each page.
  - The footer is sticky.
  - The footer contains a copyright and a link to Code Institute which opens in a new tab.

  ![Footer](static/media/readme/footer.png)

- __Register__
  - The page is intended for new users to register. 
  - The users have to enter an e-mail address, a username and the password twice.

  ![Register](static/media/readme/register.png)
  
  - After successful registration, users should receive a confirmation email.

  ![Confirmation email](static/media/readme/registration-mail.png)

  - When users click on the link in the mail, they are redirected to the email confirmation page.
  - After clicking the "Confirm" button, they will be redirected to overview.

  ![Confirm email](static/media/readme/confirm-email.png)

  - If the link is invalid or expired, an error message appears.

  ![Confirm email link expired](static/media/readme/confirm-email-link-expired.PNG)

- __Login__
  - The page is intended for registered users to log in. 
  - The users have to enter their e-mail address or username and the password.
  - When logging in, the 'Remember me' function can also be activated.

  ![Login](static/media/readme/login.png)

- __Logout__
  - The page is intended for registered users to log out. 
  - The user is asked if he/she really wants to log out before the final logout. 
  - Only after confirming by clicking on the button, the user is logged out and redirected to the home screen.

  ![Logout](static/media/readme/logout.png)

- __Lost password__
  - The page is intended for registered users to get a new password if they forgot it. 
  - Users can get a new password by clicking on the 'Forgot password' button. They will then be redirected and will need to enter their registered email address.

  ![Lost password](static/media/readme/password-reset.png)
  ![Lost password email address](static/media/readme/password-reset-sending-mail.png)

  - Users will then receive a reset link to their registered email address.
  - In this email, users will also be reminded of their username.

  ![Lost password reset mail](static/media/readme/password-reset-mail.png)

  - After clicking the link in the email, users can set a new password, which they have to type twice.

  ![Change password](static/media/readme/change-password.png)
  ![Change password confirmation](static/media/readme/changed-password-confirmation.png)

- __Overview__
  - The page is intended as an overview of the various options available on the website.
  - The page includes links to all five options: Personal data & share account, pre-existing diseases and medications, doctors, contacts and delete account.

  ![Overview](static/media/readme/overview.png)

- __Messages__
  - Messages appear for almost all relevant operations on the website, e.g. information about login, logout, add, edit, delete.

  ![Message success](static/media/readme/message-success.png)
  ![Message information](static/media/readme/message-info.png)
  ![Message error](static/media/readme/message-error.png)

- __Delete account__
  - In the overview, users will find a button "Delete account".
  - After clicking the button, users will be prompted to enter their password.

  ![Delete account page](static/media/readme/delete-account.png)

  - Only if the password is entered correctly, the account will be deleted.
  - If the input is incorrect, the user will be redirected back to the password input.

  ![Invalid password](static/media/readme/delete-account-invalid-password.PNG)
  
  - Users can also cancel the account deletion by clicking the cancel button.
  - If the password is correct, the users will be redirected to the home screen and a message appears that the account deletion was successful.
  - Users will no longer be able to log in with their old credentials.

  ![Account deletion succesful](static/media/readme/delete-account-confirm.PNG)

  - When clicking on the "Cancel" button, a modal appears and asks the users if they really want to discard their changes. 
  - If the users choose "No", they will stay on the delete page, if they choose "Yes", they will be redirected back to the overview.

  ![Delete account - modal](static/media/readme/delete-account-cancel-modal.PNG)

- __Personal data__
  - Users can see their personal data entries on this page.
  - Users can edit them at any time by clicking on the "Edit" button.
  - Users can click on the "Back to overview" button to return to the overview.
  - The "I want to be resuscitated" field is turned on by default for new users without entries.
  - The "Share account" field is turned off by default for new users without entries.

  ![View personal data - new users](static/media/readme/personal-data-new-user.png)
  ![View personal data - returning users](static/media/readme/personal-data-returning-user.png)

- __Edit personal data__
  - New users can enter their data here for the first time (first name, last name, birthday, address & city, I want to be resuscitated, share account).
  - All fields - except "share account" and "I want to be resuscitated" - are required.

  ![Edit personal data - new users](static/media/readme/edit-personal-data-new-user.png)

  - Returning users can change their entries at any time.
  - By clicking on the "Save" button, the entries are saved and the user is returned to the personal data view.
  - When users enable "share account", a randomized link is automatically generated that allows non-logged-in or non-registered users to view a non-editable overview of the user's entries in case of emergency.
  - When clicking on the "Cancel" button, a modal appears and asks the users if they really want to discard their changes. 
  - If the users choose "No", they will stay on the edit personal data page, if they choose "Yes", they will be redirected back to the view personal data page.

  ![Edit personal data - returning users](static/media/readme/edit-personal-data-returning-user.png)
  ![Edit personal data - modal](static/media/readme/edit-personal-data-cancel-modal.png)

- __Public profile__
  - When registered users enable "share account", a randomized link is automatically generated that allows non-logged-in or non-registered users to view a non-editable overview of the user's entries in case of emergency.

  ![Public profile](static/media/readme/public-profile-entries-1.png)
  ![Public profile](static/media/readme/public-profile-entries-2.png)

- __Medication/diseases__
  - Users can enter their data here (medication/disease name and instructions).
  - The field for mediation or disease name is required.
  - Clicking the "Add" button adds new entries.
  - If there are no entries (yet), this will be indicated to the users accordingly.
  - Users can click on the "Back to overview" button to return to the overview.

  ![Medication/diseases - new users](static/media/readme/medication-diseases-new-user.png)

  - If entries exist, they will be displayed to the users below the Add form.
  - For each entry there is a possibility to edit or delete it.

  ![Medication/diseases - returning users](static/media/readme/medication-diseases-returning-user.png)

- __Edit medication/diseases__
  - Users can edit their data here (medication/disease name and instructions).
  - The field for mediation or disease name is required.
  - When clicking on the "Save" button, the changes will be saved and the users will be redirected back to the medication/diseases view.

  ![Edit medication/diseases](static/media/readme/edit-medidis.png)

  - When clicking on the "Cancel" button, a modal appears and asks the users if they really want to discard their changes. 
  - If the users choose "No", they will stay on the edit page, if they choose "Yes", they will be redirected back to the medication/diseases view.

  ![Edit medication/diseases - modal](static/media/readme/edit-medidis-cancel-modal.png)

- __Delete medication/diseases__
  - Users can delete one of their medication/diseases entries here.
  - When clicking on the "Delete" button, the changes will be saved and the users will be redirected back to the medication/diseases view.
  - The deleted entry is no longer displayed.

  ![Delete medication/diseases](static/media/readme/delete-medidis.png)

  - When clicking on the "Cancel" button, a modal appears and asks the users if they are sure to cancel the delete.
  - If the users choose "No", they will stay on the delete page, if they choose "Yes", they will be redirected back to the medication/diseases view.

  ![Delete medication/diseases - modal](static/media/readme/delete-medidis-cancel-modal.png)

- __Doctors__
  - Users can enter their data here (doctor name and details).
  - The field for the doctor name is required.
  - Clicking the "Add" button adds new entries.
  - If there are no entries (yet), this will be indicated to the users accordingly.
  - Users can click on the "Back to overview" button to return to the overview.

  ![Doctors - new users](static/media/readme/doctors-new-user.png)

  - If entries exist, they will be displayed to the users below the Add form.
  - For each entry there is a possibility to edit or delete it.

  ![Doctors - returning users](static/media/readme/doctors-returning-users.png)

- __Edit doctors__
  - Users can edit their data here (doctor name and details).
  - The field for the doctor name is required.
  - When clicking on the "Save" button, the changes will be saved and the users will be redirected back to the doctors view.

  ![Edit doctor](static/media/readme/edit-doctor.png)

  - When clicking on the "Cancel" button, a modal appears and asks the users if they really want to discard their changes. 
  - If the users choose "No", they will stay on the edit page, if they choose "Yes", they will be redirected back to the doctors view.

  ![Edit doctor - modal](static/media/readme/edit-doctor-cancel-modal.png)

- __Delete doctors__
  - Users can delete one of their doctor entries here.
  - When clicking on the "Delete" button, the changes will be saved and the users will be redirected back to the doctors view.
  - The deleted entry is no longer displayed.

  ![Delete doctor](static/media/readme/delete-doctor.png)

  - When clicking on the "Cancel" button, a modal appears and asks the users if they are sure to cancel the delete.
  - If the users choose "No", they will stay on the delete page, if they choose "Yes", they will be redirected back to the doctors view.

  ![Delete doctor - modal](static/media/readme/delete-doctor-cancel-modal.png)

- __Contacts__
  - Users can enter their data here (contact name and details).
  - The field for the contact name is required.
  - Clicking the "Add" button adds new entries.
  - If there are no entries (yet), this will be indicated to the users accordingly.
  - Users can click on the "Back to overview" button to return to the overview.

  ![Contacts - new users](static/media/readme/contacts-new-user.png)

  - If entries exist, they will be displayed to the users below the Add form.
  - For each entry there is a possibility to edit or delete it.

  ![Contacts - returning users](static/media/readme/contacts-returning-user.png)

- __Edit contacts__
  - Users can edit their data here (contact name and details).
  - The field for the contact name is required.
  - When clicking on the "Save" button, the changes will be saved and the users will be redirected back to the contacts view.

  ![Edit contact](static/media/readme/edit-contact.png)

  - When clicking on the "Cancel" button, a modal appears and asks the users if they really want to discard their changes. 
  - If the users choose "No", they will stay on the edit page, if they choose "Yes", they will be redirected back to the contacts view.

  ![Edit contact - modal](static/media/readme/edit-contact-cancel-modal.png)

- __Delete contacts__
  - Users can delete one of their contact entries here.
  - When clicking on the "Delete" button, the changes will be saved and the users will be redirected back to the contacts view.
  - The deleted entry is no longer displayed.

  ![Delete contact](static/media/readme/delete-contact.png)

  - When clicking on the "Cancel" button, a modal appears and asks the users if they are sure to cancel the delete.
  - If the users choose "No", they will stay on the delete page, if they choose "Yes", they will be redirected back to the contacts view.

  ![Delete contact - modal](static/media/readme/delete-contact-cancel-modal.png)
  
  ## Future features
- For a future version, the function to change the password in the account itself could still be added.
- For a future version, the function to change the email address in the account itself could be added.
- For a future version, other registration/login options - e.g. via Google or Github - could be added.
- For a future version, even more functions could be added in the account, such as detailed instructions on what actions to take or refrain from taking in emergencies.
- For a future version, an upload function, e.g. for doctor's letters or similar, could be added.
