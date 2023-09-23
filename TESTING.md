# Testing
  * [Validator testing](#validator-testing)
  * [Automated testing](#automated-testing)
    * [Automated testing for forms in views.py](#automated-testing-for-forms-in-viewspy)
    * [Automated testing for forms.py](#automated-testing-for-formspy)
    * [Automated testing for models.py](#automated-testing-for-modelspy)
    * [Automated testing for urls.py](#automated-testing-for-urlspy)
    * [Automated testing for views.py](#automated-testing-for-viewspy)
    * [Not automated tested](#not-automated-tested)
  * [User story/Manual testing](#user-storymanual-testing)
  * [Bugs](#bugs)
    * [Fixed bugs](#fixed-bugs)
    * [Remaining bugs](#remaining-bugs)

Testing has taken place continuously throughout the development of the project. The app was tested regularly and deployed early to Heroku to confirm local and remote functioned the same.

## Validator testing

- __HTML__
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fdigital-patient-807175a8312b.herokuapp.com%2F).

- __CSS__
  - No errors were found when copy the styles.css in the official Jigsaw validator but when running the link, some issues showed up from the external library Bootstrap [Results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fdigital-patient-807175a8312b.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=de).

- __JS__
  - No errors were found when passing through the official [JS validator](https://jshint.com/).

- __Python__
  - The python-code was run through the Code Institute Python Linter and showed no errors.

  ![PEP8 Validator](static/media/readme/pep8-validator.PNG)

Google Lighthouse was used to test performance, best practices, accessibility and SEO on desktop and mobile devices.

The testing was done using the Google Chrome browser. Chrome developer tools were used extensively, particularly to check responsiveness on different screen sizes. Testing was also done using Edge and Firefox on desktop, and again on an iPad Mini and iPhone using Safari.

- Responsive on all device sizes between 280px - 2600px wide
- Devices tested using the Google Developer Tools emulator:
  - iPhone SE (375x667px)
  - iPhone XR (414x896px)
  - iPhone 12 Pro (390x844px)
  - Pixel 5 (393x851px)
  - Samsung Galaxy S8+ (360x740px)
  - Samsung Galaxy S20 Ultra (412x915px)
  - iPad Air (820x1180px)
  - iPad Mini (768x1024px)
  - Surface Pro 7 (912x1368px)
  - Surface Duo (540x720px)
  - Galaxy Fold (280x653px)
  - Samsung Galaxy A15/71 (412x912px)
  - Nest Hub (1024x600px)
  - Nest Hub Max (1280x800px)

- Desktop Results: [should be added]
- Mobile Results: [should be added]
