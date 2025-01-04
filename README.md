![The Work Logo](media/favicon.ico)

# Vintage Drums

[Andy O'Dwyer github](https://github.com/Andrewodwyer)

### Live App

[Link to Vintage Drums site](https://vintage-drum-store-6ce105a1b74f.herokuapp.com/)

### App description

<hr>
The Vintage Drum E-Commerce site is a premium online platform tailored for drum enthusiasts, musicians, and collectors seeking exceptional drums, cymbals, and accessories.

Every product is showcased with photographs and accompanied by sound recordings, enabling users to see and hear the unique characteristics of each item before purchasing.

For customers purchasing full drum kits, the site offers a premium delivery and installation service by professional sound engineers, ensuring optimal setup and performance. Additionally, free delivery is available on orders over €500 for other products.

This site is designed to provide a luxurious and user-friendly shopping experience. Shoppers can browse products by entering key words in a search bar, by category or brands, and enjoy secure checkout processes. Registered users gain access to personalised profiles with features like order history and liked products.

## Table Of Contents:
1. [UX & User-Centred Design](#ux)
    * [User Centred Design](#user-centred-design)	
    * [Target Audience](#target-audience)
    * [User Goals](#user-goals)
    * [User Stories](#user-story)
    * [Database Diagram](#database-diagram)
    * [Kanban](#kanban)
    * [Typography](#typography)
    * [MoSCow Prioritisation](#moscow-prioritisation)
    * [Epics](#epics)
    * [Story points](#story-point)
2. [UI](#ui-design)
    * [UI Design](#ui-design)
    * [Wireframes](#wireframes)
    * [Design](#design-style)
    * [Colour Palette](#colour-palette)
    * [Typography](#typography)
3. [Features](#features)
    * [Navigation](#navigation)
    * [Footer](#footer)
    * [Home page](#home-page)
    * [Products Page](#products-page)
    * [About Us](#about-us)
    * [My Events](#my-events)
    * [CRUD](#crud)
    * [DRY principles](#dry-principles)
    * [Authentication and Authorisation](#authentication-authorisation)
4. [Technologies Used](#languages)
    * [BootStrap](#bootstrap)
5. [Libraries](#libraries)
6. [Testing](#user-testing)
7. [Bugs](#bugs)
8. [Deployment](#deployment)
9. [Credits](#credits)


![Am I Responsive Image](media/readme-images/Vintage-Drum-responsive.png)

## UX
<a name="ux"></a>

### User-Centred Design Approach for planning and design.
<a name="user-centred-design"></a>

The primary goal in the planning and design of the Vintage Drum Store website is to create an intuitive, user-friendly shopping experience tailored to drum enthusiasts, musicians, and collectors. Every design decision is made with the customer in mind, focusing on showcasing the products in a way that is both functional and enjoyable to explore. From browsing drums and cymbals to secure checkout and personalised profiles, the site is crafted to offer a seamless and engaging experience at every step.

#### Target Audience
<a name="target-audience"></a>

The Vintage Drum Store is designed for musicians, collectors, and drum enthusiasts who appreciate high-quality, preowned drum kits, cymbals, and accessories. The platform serves a wide range of users, from professional drummers, seasoned musicians and collectors.

#### User Information:

- Age:

  - Professional musicians (typically 25–50 years old)
  - Drum enthusiasts and hobbyists of all ages.
  - Collectors of vintage and high-end musical instruments, often aged 30–60, who value sound quality and craftsmanship

- User Demographics:

  - Drummers
  - Collectors: People interested in rare or limited-edition drum kits and cymbals
  - Musicians who value the sound quality and history behind vintage instruments

- Location:
  Shipping throughout Ireland

#### Users’ Interests:

- Music & Performance
- Music Production & Recording: Sound engineers, producers, and session musicians

#### Regular Users:

- Drummers and Musicians
- Collectors and Enthusiasts
- Registered Users:
Regular users who create an account to track their favorite products, view order history, and save personalised profiles. They may also engage with the content of the site by reviewing products or sharing experiences with other musicians and collectors


#### How people will use the app:

- None Registered Users
  1. Browse Available Products.
  2. Search for products using key words in the search bar and selecting by category or brand.
  3. View Product Details: Users can view detailed information about each product, including descriptions, specifications, and pricing. 
  4. View addition pages "About", "FAQ" and "Home". These pages will contain any information the user will need.
  5. Enter their email to subscribe to an newsletter.
  6. Follow links to the social media pages

- Registers Users
  - They will have the same abilities as the none registered users plus the following.

  7. Personalised Profile Page: Users can create and manage their own accounts to track past orders and save favorite products.
  8. Leave Reviews: Registered users can leave review on the "About Page". The reviews have CRUD functionality. Users can add, read, edit and delete their own reviews. 
  9. Like and unlike a product.


#### Why users will use the app:

-  Product Discoverability: 
   - Users can easily search for and filter products by categories (e.g., Drum Kits, Cymbals, Stands, and Accessories), making it simple to find exactly what they’re looking for. Advanced search options allow users to narrow down results based on their specific preferences such as brand. Within each page the products can be sorted by ratings or price.

-  Personalised Shopping Experience: 
   - Registered users can like their favorite products for future purchases. Logged in users can see products they've liked in their profile page. 

- Access to Detailed Product Information:
   - The product page gives a detailed description of the product. The name, price, material, rating, description, sound recording (for drums and cymbals), sizes of drums for drum kits and an external link to the official page.

- Secure and Convenient Checkout: 
   - Users enjoy a seamless checkout experience with secure payment options. Registered users can save their payment and shipping information, making repeat purchases quick and easy.

- Order confirmation after payment on the site and a confirmation email with order details and order number

- Premium Delivery and Installation Service: 
  - For drum kit purchases, the business offers delivery and an installation service.
  - Free delivery on orders over €500, or a delivery fee based on the product with the highest delivery rate in the order. 

### User Goals
<a name="user-goals"></a>

For Shoppers: 
- Users primarily visit The Vintage Drum Store to discover high-quality, preowned drums, cymbals, and accessories.
- They want a streamlined way to browse products.
- They expect a smooth and secure checkout experience, with options to view product details, listen to sound recordings, and check delivery options.
- They want the convenience of tracking their order history, and liking their favourite items for future purchases.
- Write reviews for other shoppers and be able to edit or delete them.

For Owner/superuser: 
- The business owner uses The Vintage Drum Store to manage product listings and sales efficiently. They want a simple way to update product details, add new items, and remove outdated stock.
  - The platform’s CRUD (Create, Read, Update, Delete) functionality provides them with the flexibility to create, edit, or remove products as needed. Giving them full control over their products.
  - The owner can edit and update the about text and title as well as the products.
- They aim to provide a high-quality shopping experience for customers.
- They need tools for processing payments, adding images and managing customer feedback through reviews.
- Check orders through the admin panel. Past and present orders


### User Stories
<a name="user-story"></a>
The user stories are available on the kanban board and some will be discussed in the EPICs below.
There as three main users
- Admin/Superuser: These are the site owner that will have full control over the website.
- Registered Users: User who are logged in, allowing for more functionality 
- Non-registered users: limited functionality

### Database Diagram
<a name="database-diagram"></a>

One of the first steps in producing this app was to design and implement custom models based on the information that users would want to store and access.

An entity relationship diagram was created for planning these custom models.

As you can see from the ERD, the relationships plays a important role in how the information will be stored and accessed. Here are the main relationship and you'll also be able to view them in this Diagram

- Category model:
   - One-to-Many: A category can have many events (AddEvent model), but each event belongs to one category.

- AddEvent model:
  - One-to-Many: A single category can be associated with multiple events.
  - One-to-Many: A single user can create multiple events, but each event has one organiser.
  - One-to-Many: An event can have multiple comments, but each comment is linked to one event.

- Comments model:
  - One-to-Many: A single event can have many comments, but each comment is linked to one event.
  - One-to-Many: A single user can write many comments, but each comment is linked to one user.

- Attending model:
	- Many-to-Many: A user can attend multiple events, and an event can have many attendees.

- User:
  - One-to-Many: A single user can create multiple events.
  - One-to-Many: A single user can comment on multiple events.
  - Many-to-Many: A user can attend multiple events, and events can have multiple attendees.


![ER Diagram](media/readme-images/ERD.png)

## Kanban
<a name="kanban"></a>

For this project I created a Kansan board in GitHub to display the stages and status of each user-story. I assigned priority to each user-story using the MoSCoW method. The User-story were grouped into Epics and each User-story was given a Story Point using the T-shirt Sizing method. 

### Kanban boards in github project:
- MoSCow Prioritisation
- Epics to group user-stories
- Story Points: to estimate the work required
- Status: What stage it’s on.
- Sprints: 

## MoSCow Prioritisation
<a name="moscow"></a>

##### M: Must Have
 - Non-negotiable product needs that are mandatory.
 - Deciding factors for Must haves: 
  - What will happen if this is not included
  - Is there a simpler way to accomplish this?
  - Will the product work without it?

##### S. Should-have
-  They are essential to the product/project but they are not vital. The product will still function without it. However, the addition will add significant value. They can be scheduled for a future date.

##### C. Could-haves 
-  Nice to haves. Not necessary to the core function. They have a much smaller impact on the outcome if left out. They will be the first to be deprioritised.

##### W. Will not have
- This manages expectations and prevents scope creep. They are not expected in this specific time frame.

<br>

<details><summary><b>MoSCoW Prioritisation Image</b></summary>

![MoSCoW Prioritisation](media/readme-images/MoSCoW.png)

</details>

## Epics
<a name="epics"></a>

In a Kanban board, an epic is a large body of work that can be broken down into multiple smaller user stories and tasks. The user stories have been grouped into 5 epics based on core functionalities for different user types and areas of the platform. The purpose of dividing them this way is to ensure that each set of features aligns with specific user journeys, from product browsing to checkout and administration.

Below is a description of each epic:

#### Epic 1: Product Browsing (Shopper)

This epic is focused on providing a seamless experience for shoppers exploring the products on the site. The features here prioritize discoverability, ensuring that users can easily find and learn about the products they are interested in.

- Abilities:
  -	View products by category and view product details to easily navigate and understand the product range.
  -	Search and filter functionality is essential for quick access to specific products or categories.
  -	Product images and recordings (If available), see and hear products.

- Example User Stories:
  -	As a shopper, I want to be able to easily see what I’ve searched for and the number of results so that I can quickly decide whether the product I want is available.
  -	As a shopper I want to see the item in the shopping bag so that I know what I've already added

#### Epic 2: Bag Management and Checkout (Shopper)

This epic focuses on the features that enable users to add products to their cart, manage their shopping bag, and complete the purchase securely. It covers the checkout flow and essential functionality for users to complete a transaction.

- Abilities:
  -	Adding and editing items, adding additional items if they are stick or stands. Delete Items from basket.
  - Secure payment and order confirmation.
  -	Email confirmation.
  - Subscription option.
  - They have CRUD functionality
    - Adding a product
    - adding additional quantity if they are stick or stands.
    - Delete Items from basket.

- Example User Stories:
  - As a shopper, I want to edit the contents of my bag so that I can update quantities, sizes, or remove items.
  - As a shopper, I want to receive an email confirmation after checking out so that I can keep the confirmation of what I’ve purchased for my records.

#### Epic 3: User Accounts (Registered Users)

It enables shoppers to track their orders, manage personal information, and save preferences.

- Abilities:
 - Account registration and login.
 - Personalised profiles allow for customisation, while features like viewing past orders and liking products enhance the user’s ability to track and save their favorite items.
 - Password recovery ensures users can always access their accounts.

- Example User Stories:
	- As a site user, I want to view my past orders so that I can reference my previous purchases.
	- As a registered user, I want to edit my profile information so that I can update outdated details.
  - As a registered user, I want to log in and out of my account so that I can access my profile and order history.

#### Epic 4: Admin Tools (Admins/Superusers)

The Admin Tools epic is aimed at giving administrators and superusers the ability to manage products, content, and user-generated elements of the site. This epic ensures that admins can maintain and update the site’s content efficiently.

- Abilities:
 - Access to the admin panel, and the ability to add, edit, and delete products.
 - Uploading product images and add details of products.
 - Keep track of reviews and approve them.
 - Monitoring sales and orders.
 - Update website content like the About page and FAQ page.

- Example User Stories:
	- As an admin, I want to delete a product so that I can remove items no longer for sale.
	- As an admin, I want to access the admin panel so that I can manage the website’s content.
  - As an admin, I want to add, edit, or delete FAQs so that users can access up-to-date information.

#### Epic 5: Sorting and Searching

The Sorting and Searching epic is designed to make product discovery as intuitive and fast as possible.

- Abilities:
 - Search using key words in the search bar. Words in title or body
 - Search by brands

- Example User Stories:
	- As a shopper I want to select a brand so that I can see all the product of that brand that are in stock
	- As a shopper, I want to search for a product by name or description so that I can find a specific item.

Each of these epics groups together the relevant user stories under a common theme, making it easier to manage and visualise progress on the Kanban board. The Epics are grouped using Tags on the User Stories eg. Tag: "Product Browsing (Shopper)"

![Kanban Board](media/readme-images/Kanban-Board.png)

[View Kanban Board here](https://github.com/users/Andrewodwyer/projects/7)


## Agile Story points
<a name="story-point"></a>

Story points are a unit of measure used in Agile project management in Scrum, to estimate the relative effort or complexity of user stories or backlog items.
Instead of estimating in terms of time (e.g., hours or days), which can be subjective and vary based on individual team members’ skill levels, story points focus on the overall effort or complexity involved. Story points represent a combination of factors, including the effort required, technical complexity, risks, and dependencies.I have used T-shirt Sizing for this.

- Some example of using Story Points:
	1.	User Story: “View item in Bag”
	 - T-shirt Size: S (Small), Story Points: 2
   - Reason: Not a lot of function set up required.

  2.	User Story: “Safe and Secure Payment”
	 - T-shirt Size: L (Large), Story Points: 4
   - Reason: Integration of Stripe is a long process.

  3.	User Story: “Approve Reviews”
	 - T-shirt Size: M (Medium); 	Story Points: 3
	 - Reason: I have done this in project 4 and setting up the process for adding review and approving them in the admin is not too time consuming

By using T-shirt size Agile story points, you can effectively estimate the workload for each epic and user story

</details>

### Sprints
Two-week sprints provide a manageable and focused time frame, promoting iterative progress and allowing quick adjustments based on feedback. This rhythm ensures regular deliverables, promotes agile development, and allows for more efficient planning, testing, and review within each sprint. This project used 5, 2 week sprints. After each sprint the work was evaluated and tasks and user stories were moved onto the following sprint if they we're finished.

1. Sprint 1: Design and Core Functionality Setup
2. Sprint 2 Sorting and Searching
3. Sprint 3: Shopping bag and Checkout
4. Sprint 4: User Experience
5. Sprint 5: User flow, test, UI

![Sprints](media/readme-images/Sprints.png)

<br>

## UI Design
<a name="ui-design"></a>

The initial wireframe was designed using figma. The figma project page can be found here [FIGMA VINTAGE DRUMS](https://www.figma.com/design/b4pEB6Sa7kAI28JAD907yr/music-store?node-id=0-1&p=f&t=lBdudrK7G6AQKPRc-0)

## Wireframes
<a name="wireframes"></a>

#### Mobile Wireframe

![mobile wireframe](media/readme-images/mobile-wireframe.png)

#### Desktop Wireframe

![Desktop wireframe](media/readme-images/desktop-wireframe.png)

### Design Style
<a name="design style"></a>

The UI design for the app was to be a modern, clean and userfriendly. Balancing functionality and aesthetics, so the user can easily navigate through the app.

### Colour Palette:
<a name="colour-palette"></a>
- Primary Background Colours: White (#FFFFFF) & Off-White (#F8F9FA)
  - These light, neutral shades ensure the site feels open and spacious, making it easy for users to focus on the products without visual distractions.
- Footer Colour: Dark Charcoal (#2A2A2A)
  - The footer is a rich charcoal grey that provides a clean, grounded contrast against the lighter background.
- Main Action Button: Teal-Green (#49A299)
  - The colour gets attention without overwhelming the design, and it works well with the neutral tones of the background.
- Hover Button: Copper-Gold (#B0882F) on the Dark Charcoal Footer.
  - Giving a premium, tactile feel.
- 

<hr>

![Colour Palette](media/readme-images/colours.png)

### Typography:
<a name="typography"></a>
- Roboto

These are modern style fonts that work well with the clean, minimal design.

### Logo
- Vintage Drums

- I used favicon.io to create the “VD” icon for the website. The colour and font matching the design.

### Favicon

- Designed in favicon.io

## Features:
<a name="features"></a>
### Navigation
<a name="navigation"></a>

- Navbar on Desktop:
  - On desktop, the navigation bar is horizontally aligned across the top of the page, ensuring that users can quickly and easily access each section of the site. The dropdown menus are simple and clear with subtle hover effects that indicate interactivity. The My Account dropdown dynamically changes depending on the logged-in status of the user (superuser or registered user). The shopping bag icon is prominently displayed on the right, ensuring users can easily access their cart at any time.

  - Icons for shopping cart and user makes it easy for users to navigate.

![Navbar](static/readme-img/UX/navbar-desktop-mobile.png)

- Navbar on Mobile:
  - On mobile devices, the navbar is designed with responsiveness in mind, ensuring that users can still easily navigate the site on smaller screens.

  - Clicking on the hamburger icon reveals the full list of options, with dropdown menus that allow users to filter products by categories or brands. These menus are scrollable, ensuring users can access all available options even on mobile.
  - The My Account dropdown and Register/Login options are still available in the mobile version, with a similar dynamic interface depending on whether the user is logged in.
  - The shopping bag icon remains prominently placed on the top right, giving users easy access to their cart from anywhere on the site.


### Footer:
<a name="footer"></a>
- The footer provide users with essential information and easy access to key features, such as subscribing to the newsletter, accessing social media links, and navigating other parts of the website.
- Features:
  - Newsletter Subscription via Mailchimp
  - Social Media Links
  - Information Links: About Us, Privacy Policy, FAQ

![Footer](media/readme-images/footer.png)


### Home Page
<a name="home-page"></a>

- Logo displaying the brand, immediate recognition of the app. Users feel more comfortable when they are reassured by the brand.
- Hero section. Image of a drum kits and text "Uncover the Soul of Vintage Drums" and "Curated collection of premium vintage drum kits and cymbals for musicians and collectors." Highlights the purpose of the app
- Category & Links discussed earlier


### Products Page
<a name="products-page"></a>

- Grid Layout for Products. Each page contains 6 products so not to overwhelm the user
- Pagination button, to navigate to the next or previous page
- Sort by: This option on right of the screen allows the user to choose if they like to sort by price or rating
- A button at the top of the products indicates which category they are viewing

### About Us
<a name="about-us"></a>
- A form for the user to add their event details
- Displayed using Crispy-form
- Image upload using cloudinay
- Once the event is submitted, a message displays to indicate to the user that the event has been submitted.
- If the form is missing required information or if it has not been filled out correctly, a message will display regarding the issue to correct.


### My Events
<a name="my-events"></a>
- A grid display of your events as cards, like the home page
- Events that are not published/ in drafts have a transparent element over then to indicate that it is not published. Image below
- Both published and draft events can be clicked on and edited/deleted
- If the user is not logged in, they will be brought to the sign in page

![My Event Draft Display](static/readme-img/UX/draft-event.png)


### Register
- Sign up page if the user does not have an account
- A form page that requires: username, email(optional) password and password confirmation. Details regarding passwords are displayed
- A message will be displayed if the there is an error with the form.
- When registered, the user will then be redirected to the home page with a message "Successfully signed in as USERNAME."

### Log out
- This page contains a message "Are you sure you want to sign out?" and a button
- The user is redirected to home page after signing out

### log in
- Message displayed in a container
- Container with form for username and password.
- Sign in button will direct the user to the home page if the form is correctly filled out.

### 404
- I created a 404 page in the event templates. As it was not in the app directory but in templates it would be displayed if there was an 404 error. This is a built in django feature. I used the base.html template, an image and a message to allow the user to navigate back to the home page.

<details><summary><b>404 page</b></summary>

![404 page](static/readme-img/UX/404-page.png)

</details>



## CRUD
<a name="crud"></a>
The Events App’s CRUD functionalities for events, comments, and attending are designed to give logged in users control over their interactions with the app.
The list below has CRUD abilities for the registered user
| **Entity**    | **Create**                               | **Read**                                   | **Update**                               | **Delete**                               |
|---------------|------------------------------------------|--------------------------------------------|------------------------------------------|------------------------------------------|
| **Events**    | Event organisers can submit new events.   | Users can view event lists and details.     | Organisers can edit their own events.    | Organisers can delete their own events.  |
| **Comments**  | Logged-in users can post comments.        | All users can view approved comments.       | Logged-in users can edit their own comments.       | Logged-in users or admins can delete comments.     |
| **Attending** | Logged-in users can RSVP to an event.               | Logged-in users can view attendance.   | Logged-in users can change their RSVP status.      | Logged-in users can remove their RSVP.             |

## DRY principles
<a name="dry-principles"></a>

#### Three main benefits: Reusability, Maintainability & Customisation

### HTML Template inheritance

#### base.html

The base.html keeps the look and feel of the site consistent. 
Template inheritance goes hand in hand with DRY principles - Don't Repeat Yourself. Using inheritance, we only need to write them once. After that, we can inject the content from each page into named blocks. {% block content %}

This extends tag {% extends "base.html" %}  tells each .html that it is a child template of base.html. Unique html to each page is injected into the base.

I use this base.html for all pages to create the same look and feel for all our pages. The base.html template however is not the only one that can be reused. After writing each pages Html I saw there was other pages that could reuse code. There pages were
- index.html (home page)
- events_by_category.html
- my_events.html

#### Pagination:
Pagination, meaning "divide up into pages”.
paginate_by = 6,  tells Django to display 6 posts at a time.
is_paginated is a boolean (set to true) more than the paginate number that was set to 6, add pagination. paginate number was set in the app view.py
    template_name = "event/index.html"
    paginate_by = 6
I first used this just on the index.html (home) page. As the same pagination would be used on 3 html pages (index.html, events_by_category.html and my_events.html) I decided to place the pagination in its own template called pagination.html and include it in those 3 pages using the {%include%} tag.        
{% include "event/pagination.html" with page_obj=page_obj %}. 
The page_obj contains the current page’s events and pagination details if there is a next or previous

#### Event Card Display
Like the Pagination on these pages the majority of the code was the same. The only major difference was the h3 element at the start of the page and a message that displays at the end of the page {%if%} statement
The card_display.html template was created in response to this. This template used the code that was duplicated on each page. These pages are free of clutter and the card design need only be changed once in the event-card.html and would apply on all the relevant pages that had the {% include "event/event_card.html" with event=event %} tag.

![Pagination cards and buttons](static/readme-img/UX/pagination-6-card-and-button.png)


### Cards
- In keeping with the dark background the cards are white to standout, indicating importance. 
- The card displays an image with text under it. There is a "Learn more" link element that is a "signifier" to click to view more information. I saw this style link on apples website. The classic blue style link is a perfect signifier, separating itself from the other text.
- I have made the whole card a link even though it looks like the blue "Learn more" is the link. This was done to make it easier for the user to move to the next page. All designed with the user in mind. 
- There is a slight drop shadow on the cards as well to elevate it.


### Buttons and Icons
<a name="buttons-and-icons"></a>
The action buttons like sign up, edit, delete and next/previous are solid colours when inactive and white with colour text and border when hovered over.
This was due to the type of button is was. Once clicked they were gone. 
- The icon buttons for the categories and attending buttons are differnet however. 
  - The categories are on a white bar and would be distracting if they were block colours initially. Once a category is active its colour needs to inform the user of their location with a obvious sign. A quote from Steve Krug from his book "don't make me think" 
    - “The fact that the people who built the site didn’t care enough to make things obvious—and easy—can erode our confidence in the site and the organization behind it.”
  - Icons provide a visual shortcut

- The icons are from [fontawesome](https://fontawesome.com/)
<hr>

![Category buttons](static/readme-img/UX/category-button.png)


![Action button with edit:hover](static/readme-img/UX/edit-button-hover.png)


### Design familiarity
  - Attending button: Just like the categories buttons, this had to be obvious. There are many apps with this idea of liking or attending. This grey to green concept is intuitive. This leverages the users prior experiences, making it feel familiar and natural.
  <hr>

![Attending Button](static/readme-img/UX/attending-icon.png)


### Authentication-Authorisation, User Interaction with messages & signafiers
<a name="authentication-authorisation"></a>

- Authentication is the process of verifying a user’s identity when they log in or register for the first time.
  - Django Allauth is used for user authentication and registration, providing pre-built views and forms for registering new users.
- Authorization defines what a user is allowed to do once authenticated. In this app, different actions are available based on whether the user is logged in and whether they've created the event, wrote the comment or RSVPed.

- Information/Messages: When an action is preformed, like creating a comment or event, a relevant message displays to the user. These are styled to blend smoothly into the page without overwhelming the user.
- Authentication Indicators: Users are reminded whether they are logged in or not through a simple text message displayed to the left of the screen near the header.

![Messages and signafiers](static/readme-img/UX/Message-signafiers.png)

### Bootstrap
<a name="bootstrap"></a>
Bootstrap was used in the app to create a responsive, mobile-first websites quickly and efficiently using it's library. Bootstrap provides a collection of pre-designed HTML, CSS, and JavaScript components, like buttons, forms, navigation bars, and grid layouts. By using Bootstrap, I was able to build a visually consistent app without writing extensive custom code. It was easy to customise and it adapted to all screen sizes without having to write additional media queries. Saying this, I did customise the css and added js in this build.


### Additional App Features
<a name="additional-features"></a>
1. Event Browsing and Filtering 
- Filter by category
- Filter by calendar view. Events are displayed in the calendar dates
- View the events you've created

2. User Authentication
- Users can register, sign in and sign out
- Registered users have additional benefits: add events, comments and indicate attendance

3. Create Events
- This feature encourages users to actively contribute on the app, creating a sense of community and ownership. 

4. Category Icon:
- Discuss earlier

5. Interactive Calendar View
- Users can see upcoming events on a specific date
- Clicking the event title (link) brings the user the event details page
- Beneficial for users that only want to see events by date that they're available for.

![Calendar View](static/readme-img/UX/calendar-view-desktop-mobile.png)

6. Event Interaction
- Mark as Attending
- The click icon turning from grey to green provides a sense of accomplishment and interaction enhancing the user experience

7. Comments
- Organiser can update the event with a comment.
- A user can ask a question or comment.
- Benefits to the user as they feel more connected to the event

8. Social Media
- Links to social media were the app and event can be more visible 

9. Image display. 
- The organiser when creating the event can add their own image. 

10. Additional information from the Organiser aids to better Search Engine Optimisation


### Libraries
<a name="libraries"></a>

- Django-cloudinary-storage: handling the images
- Crispy-forms: making it easier to work with forms, providing better rendering and handling.
- Django-summernote: Handling text
- Crispy-bootstrap5==0.7 - A Crispy Forms template pack for Bootstrap 5

### Manual Testing user stories

<a name="user-testing"></a>

User Story |  Test | Pass
--- | --- | :---:
As a Site Admin I can view comments on an individual post so that I can read the conversation | In admin panel click on comments tab and select comment | &check;
As admin I can mark addevent and comment requests as read so that I know which ones I've seen | In admin panel click on comments tab and select box at the start of the comment | &check;
As the Admin I can view event request and comment requests, so that I can review and approve them | In admin panel click on comments tab or Add events tab and select item event or comment you'd like to review and approve | &check;
As a Registered User, I want to indicate my attendance to events so that others know I’m planning to go. | Login, select event, click on the attending icon | &check;
As a user/event organiser I can view all the events I've created so that I can manage them | login, in the nav bar click My Events, select one of your events | &check;
As a user I can see the nav-bar so that I can easily go back to the home screen | Only when events are no longer available, past events that are moved to draft or deleted | &check;
As a user I can log in to my account so that I can add events | log in, click the link Create an Event, fill in form and submit | &check;
As a site user I can create, update and delete events | Once logged in, click on My Events page, select the event to edit or delete. Once in the details page, press the edit or delete button, delete button will display a modal to confirm delete. Edit button will bring you to a form page with the current input information. Edit event details and submit. If selecting delete, a bootstrap modal is shown with two buttons, close and delete. Close, closes the modal, delete deletes the event| &check;
As a Registered User, I want to comment on events so that I can share my opinions or ask questions. | login, select the event you'd like to comment or ask a question to, and click submit | &check;
As site user I can view events in a paginated way so that I can select one that interests me. | on the home page, category page or my events page, you'll see a button under the events. The button is numbered relating to current page and an arrow for next or previous | &check;
As a user I can open a event listing from the calendar so that see more details of the event | Click on the Calendar button on the nav-bar, select the date that has a event listed by title. Click title and you'll be brought to that event details page | &check;
As a User, I want to browse and search for events by category so that I can find events that interest me. | User chooses a category from the category tab. Choose one of the four buttons. User sees a new listing of filtered events by that category| &check;
Sign up prompt. As a non-registered user I can register for an account so that I add events, write comments & show attendance | Non logged in users will be directed to the sign in page when click create an event, my events or indicate attendance | &check;
As a user/ site visitor, I want to browse events without needing to register so that I can see what’s happening in my area. | all users can see the events by all, category and calendar | &check;

### User registration, sign in and log out
![User registration, sign in and log out](static/readme-img/UX/Sign-Up-sign-in-sign-out.webp)

### Manual Testing features

| Feature | Action | Status | 
|:-------:|:--------| :--------|
| Register | Selected Register on the nav menu, input Username, Email(optional), password, password again to confirm they are identical, click sign up. Redirected to home page if correctly done. Message to show what additional steps if not successful | &check; |
| Login | Select Login from the nav menu, input username and password, click Sign in button. Redirected to home page if no issues. A message "The username and/or password you specified are not correct." if you are a new user or inputs are incorrect | &check; |
| Logout | Select logout from nav menu, click sign out, redirected to home page | &check; |
| Filling in create event form | Registered users click create an event button, Fill in the required fields in the form, submit event. There is a message to indicate that the event was successfully created. If there is an issue with the required fields, a message will be displayed to show the issues | &check; |
| Add a comment to an event | In the event details page under the event description is a comment field. Make a comment and click the button submit. The user will be returned to that event page and a message will be displayed so the user knows the comment has been sent to be reviewed before being published | &check; |
| Edit and delete comment | This created comment can be edited or deleted by the comment writer. They will see two buttons, edit and delete. Clicking edit will display the previously submitted commend in the comment field to be edited and submitted again. Clicking delete will bring up a bootstrap modal to confirm delete. Two buttons are displayed on the modal. close or delete | &check; |
| Social media links| links in the footer takes the user to the relevant websites | &check; |
| Admin panel view | add /admin to the end of the home url to see admin panel. Admin panel is only available to the admin and not a regular user | &check; |
| Admin Display | Once in the admin panel, they will be able to view 3 columns, first for options, middle for description and right for filter | &check; |
| Link to events page added in form, available in event details | The link can be added to the field in the form and the link is available in the event details page. The link is to open a new tab with the link | &check; |
| Image Upload | In the Create an Events form a image can be uploaded to cloudinary and available to display on the events details page and event card | &check; |


![Delete modal](static/readme-img/UX/delete-event-modal-bootstrap.png)

### User flow test, Happy path for new user
A happy path covers the core functionality and user experience of the event app, ensuring smooth navigation, registration, and interaction with events.


| Action | Expectation | Pass | 
|:-------:|:--------| :--------|
| The user navigates to the home page of the events website | All upcoming events are displayed in a list. Category filter buttons (e.g., “Music,” “Art,” etc.) are clearly visible in the navigation bar. | &check; |
| The user clicks the “Music” category button to filter the events | The list of events updates to show only music-related events. The user sees events related to the “Music” category. | &check; |
| The user clicks on an event that interests them to view more details. | The user is taken to the event detail page. Information about the event (title, date, time, location, description) is displayed. A prompt to log in or register is visible for users who want to indicate attendance. | &check; |
| The user navigates to the calendar page, as they want to check events on a specific date. | A calendar view is displayed, showing events for the current month (October). Events are marked on the calendar with clickable dates. | &check; |
| The user changes the month to November and clicks on the 1st. | The calendar updates to show events in November. The user sees the “Urban Art Expo” event listed on November 1st at 11 AM | &check; |
| The user clicks on the “Urban Art Expo” to view the event details. | The user is taken to the event detail page for the “Urban Art Expo.” The event’s full details are displayed (title, date, time, location, description). | &check; |
| The user clicks the “Register” button to create an account. | The user is directed to the registration form. Fields for username, email, and password (with confirmation) are visible | &check; |
| The user fills in the registration form, username: “John” and submits it. | The user is redirected to the home page. A notification appears saying “Successfully signed in as John.” | &check; |
| The user navigates back to the “Urban Art Expo” event and clicks the attendance button/icon. | The attendance icon turns green. A visual confirmation, a message and a change in the icon’s appearance, shows that the user has successfully indicated attendance. | &check; |
| The user scrolls down to the comment section and types the question: “Will this event be appropriate for children?” | The comment form is visible, and the user can submit the comment. After submitting, the page reloads with a message saying, “Comment submitted and awaiting approval” | &check; |
| The user sees a mistake in the text and want to change it | The user clicks the edit button. The current text displays in the form. The text is updated. User submits the form. After submitting, the page reloads with a message saying, “Comment Updated!” | &check; |
| The user sees the confirmation message for the comment and decides to leave. | The user is satisfied with the process and expects their comment to be reviewed. They leave the site, planning to return later to check for responses. | &check; |

### User flow test, Happy path for event creator

| Action | Expectation | Pass |
|:-------:|:--------| :--------|
| The user clicks the "Login" button. | The login form is displayed, and the user logs in successfully. | &check; |
| The user navigates to the "My Events" page. | The user sees a list of their current event listings. | &check; |
| The user clicks the "Create an Event" button. | The user is taken to the event creation form with empty fields. | &check; |
| The user fills out the event form but enters the wrong end date (before start date). | The form reloads, and an error message appears under the "End date" field saying, "The end date & time must be after the start date & time." | &check; |
| The user corrects the end date and submits the form. | The user is redirected to the home page with a notification: "Add event request received! It will be reviewed within 2 days." | &check; |
| The user goes back to the "My Events" page. | The newly created event is listed but faded with a message saying, "This event is in drafts. Click to update." | &check; |
| The user clicks on the draft event to review it. | The user sees the event details and how it will look when published. | &check; |
| The user decides to edit the price and clicks "Edit Event." | The user is taken back to the event form with pre-filled details from the previous submission. | &check; |
| The user scrolls down, changes the price to 30, and clicks "Submit." | The event is updated, and the new price is reflected in the event details. | &check; |
| The user checks the event status the next day. | The event is now live and visible to all users, no longer faded in the "My Events" page. | &check; |
| The user marks their intention to attend their own event. | The attendance icon turns green, and a visual confirmation is shown that the action was successful. | &check; |
| The user leaves the site. | All actions were completed successfully, and the event is live. | &check; |

### Validator Testing 

### HTML

All pages have been passed through the W3C validator. The only page that had an error was the the sign-up page
Django Summernote issue: It's a known bug that adds extra paragraph tags to the body content in the posts.
I’m aware of the issue/bug coming from Django Summernote.

[W3C validation](https://validator.w3.org/#validate_by_input) was used to check the markup validity of html file.

<details><summary><b>Home page, passed</b></summary>

![Home page](static/readme-img/code-validated/Home-index-html-checker.png)

</details>

<details><summary><b>Add/Create an Events page, passed</b></summary>

![Create an event](static/readme-img/code-validated/Add-event-html-checker.png)

</details>

<details><summary><b>Events Details, passed</b></summary>

![Event details](static/readme-img/code-validated/Event-details-html-checker.png)

</details>

<details><summary><b>Events Details with description fields containing a number of paragraphs, passed.</b>No errors but some warnings relating to paragraphs in larger description fields when the entry contained a number of paragraphs. This is a know summernote warning. The paragraph elements are in a 'article' element so they do not produce and error.</summary>

![Event details](static/readme-img/code-validated/event-details-warning-paragraphs.png)

</details>

<details><summary><b>Calendar page, passed</b></summary>

![Calendar page](static/readme-img/code-validated/Calendar-page-html-checker.png)

</details>

<details><summary><b>Events by category page, passed</b>Events by category page, passed</summary>

![Events by Category page](static/readme-img/code-validated/categories-html-checker.png)

</details>

<details><summary><b>My events page, passed</b></summary>

![My events page](static/readme-img/code-validated/my_events-html-checker.png)

</details>

<details><summary><b>Login page, passed</b></summary>

![Login page](static/readme-img/code-validated/Login-html-checker.png)

</details>

<details><summary><b>Sign up, 4 errors. Known summernote issues</b></summary>

![Sign up](static/readme-img/code-validated/Sign-up-html-checker.png)

</details>

<details><summary><b>logout page, passed</b></summary>

![Logout page](static/readme-img/code-validated/logout-html-checker.png)

</details>


### CSS

No CSS issues

[Jigsaw](https://jigsaw.w3.org/css-validator/#validate_by_input) was used to check css files

<details><summary><b>style.css</b></summary>

![Logout page](static/readme-img/code-validated/css.png)

</details>

### JavaScript

[Jigsaw](https://jigsaw.w3.org/css-validator/#validate_by_input) was used to check css files

Calendar.js 
- When testing the calendar js an error of undefined variable FullCalendar. FullCalendar is a django library. new FullCalendar.Calendar is called to create a new calendar instance,in the html id=calander.

eventsComments.js
- When testing the eventComments js an error of undefined variable Bootstrap. Bootstrap is a Django library. new Bootstrap.Modal creates a modal instance and provides the functionality to interact with that modal.


<details><summary><b>attendance.js</b></summary>

![attendance.js](static/readme-img/code-validated/attendance.js-check.png)

</details>

<details><summary><b>calendar.js</b></summary>

![calendar.js](static/readme-img/code-validated/calendar.js-checker.png)

</details>

<details><summary><b>eventsComments.js</b></summary>

![eventsComments.js](static/readme-img/code-validated/eventsComments.js-check.png)

</details>

### Python

#### PIP8 Compliant


| File                   | Result |
|------------------------|--------|
| settings.py            | Pass AUTH_PASSWORD_VALIDATORS line too long|
| urls.py                | Pass   |
| admin.py               | Pass   |
| manage.py              | Pass   |
| apps.py                | Pass   |
| forms.py               | Pass|
| models.py              | Pass   |
| Project urls.py        | Pass   |
| wsgi.py                | Pass   |
| asgi.py                | Pass   |
| Models.py              | Pass   |

The 4 lines in setting.py that are too long is the AUTH_PASSWORD_VALIDATORS. There are automatically generated and can be left. All other python files passed.
<details><summary><b>Settings.py CI Linter result</b></summary>

![Settings.py CI Linter](static/readme-img/code-validated/settings.py-ci-linter.png)

</details>

[CI Python Linter](https://pep8ci.herokuapp.com/) was used to check the validity of python files.

### Google's Lighthouse Performance
<a name="lighthouse"></a>
I checked the app for Performance, Accessibility, SEO and Best Practices using google's Lighthouse
Over all I was please with the results:
- Accessibility: 100%
  - Accessible to screen readers
  - Sufficient colour contract for readability
- SEO: 100%
  - Properly structured data, mobile optimization, and fast loading times
- Performance: 99% & 93%
  - Fast performance
  - Image sizing
- Best Practice: 79%
  - Third party warnings because of using cloudinary for the images. Google Chrome indicates issues with web standard and future-proofing of the site. "Support for third-party cookies will be removed in a future version of Chrome".
  - This will be something to resolve in the future but for now cloudinary is the best option for users to upload images to their event. 
  - It would not be an option to not use cloudinary as without the ability to use images to make their events stand out and be immediately visable with brand recognition, user would not engage with the site fully. They could see less rewards for their time.


![Lighthouse Performance](static/readme-img/code-validated/lighthouse-score.png)


### Browser Compatibility
<a name="browser"></a>
The Following Browsers were checked:

- Google Chrome
- Safari
- Opera
- Firefox
- Microsoft Edge

On all browsers the site performed smoothly with consistent functionality and appearance. All features were tested and worked as expected.

### Responsiveness
<a name="responsiveness"></a>
The app is responsive on all screen sizes. The event card display using bootstrap is shown above (at the start of the read me) and the calendar view (in the calendar description).
The image below will show the event details page and create events form.

![Responsiveness](static/readme-img/code-validated/Responsive_test.png)


## Languages
<a name="languages"></a>
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Provides the functionality for the site.
- [HTML5](https://en.wikipedia.org/wiki/HTML) - Provides the content and structure for the website.
- [CSS3](https://en.wikipedia.org/wiki/CSS) - Provides the styling for the website.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - Provides interactive elements of the website


## Frameworks & Software
<a name="frameworks-software"></a>
- [Gitpod](http://gitpod.io) - Cloud based IDE
- [Bootstrap](https://getbootstrap.com/) - A CSS framework that helps building solid, responsive, mobile-first sites
- [Django](https://www.djangoproject.com/) 
- [Figma](https://www.figma.com/) was used to create the final design of a website.
- [Github](https://github.com/) - Used to host and edit the website.
- [Heroku](https://en.wikipedia.org/wiki/Heroku) - A cloud platform that the application is deployed to.
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) - Used to test performance of site.
- [Font Awesome](https://fontawesome.com/) was used for social media icons in the footer.
- [Favicon](https://favicon.io/) was used for favicon.
- [LucidChart](https://lucid.co/) was used for creating ERD.
- [Google Fonts](https://fonts.google.com/) was used to add specific font family to the stylesheet.
- [W3C validation](https://validator.w3.org/) was used to check the markup validity of html file.
- [Jigsaw](https://jigsaw.w3.org/css-validator/) was used to check the validity of css file.
- [JSHint](https://jshint.com/) was used to check the validity of js files.
- [CI Python Linter](https://pep8ci.herokuapp.com/) was used to check the validity of python files.
- [Am I Responsive](https://ui.dev/amiresponsive) was used to get a screenshot of a final look of the website on various devices.
- [Github](https://github.com/) was used to store the code of the website.
- [Django](https://www.djangoproject.com) used as the Python framework for the site.
- [PostgreSQL](https://www.postgresql.org) used as the relational database management.
- [Cloudinary](https://cloudinary.com) used for images
- [Gunicorn](https://gunicorn.org/) used for WSGI server
- [Crispy Forms](https://pypi.org/project/django-crispy-forms/)
- Photoshop: Resizing and editing pictures


### Create a PostgreSQL Code Institute database
<a name="postgreSQL"></a>
- Log into [CIdatabase maker](https://dbs.ci-dbs.net/)
- Add your email address in input field and submit the form
- Open database link in your email
- Paste dabase URL in your DATABASE_URL variable in env.py file and in Heroku config vars

### Cloudinary
<a name="cloudinary"></a>
- Navigate to https://cloudinary.com/ and log in to your account.
- Navigate to dashboard/console https://console.cloudinary.com/console/  copy API Enviroment variable starting with "cloudinary://".
- Paste copied url CLOUDINARY_URL variable in env.py file and in Heroku config vars
- Update settings.py

### Django secret key

You need to include you Django secret key that you can generate using any of the Django secret keys generators online.
In order to protect django app secret key it was set as an enviroment variable and stored in env.py.

```
os.environ.setdefault(
    "SECRET_KEY", "your secret key")
```

## Bugs:
<a name="bugs"></a>

#### Category Migration 
-  I had to roll back the migrations from 0006 to 0003, using the terminal command
  python3 manage.py migrate events 0003 
  This was because I had set a default=“music” in the AddEvents model and had made a migration. The default had to be an integer so I checked what ID music had. This was done by using this command in the shell.
  from event.models import Category
  music_category = Category.objects.get(id=1)
  print(music_category.name)
  The result id was 1.
  I updated the code to reflect this. Below code, default=‘Music’ is now default=1
      event_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='events', default=1)
  This still didn’t resolve the issue. When trying to make a migration using the integer 1 I was given an error of database is expecting a integer and instead got ‘Music’.
  I rolled back the migrations, deleted the last 2 migrations and made a new makemigration and migrate. 
  This resolved all the issues. I did have to set the categories in the admin panel again.

#### Load Static bug
-  I had used Django Template Language tag to include the images in the static directory for the events template html file but I didn’t do the same for the index.html file. Once I did this the images loaded as intended.

#### Categories in events bug
-  Fixed the bug in event_by_category.html, the loop was category in categories but it should of been events in events to show the events with the category_id, ie music has a category id of 1
  I used a function in the view.py called event_list_by_category and it got the Category object from the AddEvents 

#### Load Static in events_by_category.html bug
-  The static images on the events_by_category.html file weren’t loading and this gave me an error indicating it was expecting a {%endfor%} tag as it couldn’t see the static folder.
  This was easily fix by adding the {% load static %} tag at the top of the html file

#### Pagination for function based views Bug
-  Pagination for function based views. I was trying to add a function that used paginator = Paginator(events, 6). Because it was a function and not a generic class I had to add page_obj and is_paginated Django tags in a certain sequence. The issue was the page_obj wasn’t properly accessed in the template, which is causing the issue with the pagination displaying "Page of ." with no next or previous buttons. I consulted https://docs.djangoproject.com/en/5.1/topics/pagination/ and tried a number of different options but it didn’t work. In the EventList class the generic ListView automatically handles context variables like page_obj for pagination. I decided to use a generic list view class for the categories html template too.
  To have a simple class view I needed to set up a function that filtered the events by category and by current and future dates. For the dates I used the class AddEventManager(models.Manager): in the models.py that filtered by time. and set it’s status to 1 (published). Then I used the .filter(event_category=category) that got the category.

#### Loading Image in the index.html and then the addevent_detail.html
-  img src was different for index.html and addevent_details.html. This was because of the for loop {% for event in addevent_list %} in index which took the name addevent_list from the generic.ListView class EventList. While addevent_details.html used the variable name addevent. When I used the variable name addevent in the index.html it didn’t load because or the for loop. I decided to make a note of the issue and review it if needed.


#### Model issues: Comments and AddEvents user/organiser field Bug
-  In the AddEvents model I used ‘organiser’ as the field for the user. However in the Comment model the field was ‘user’ for the user and not ‘organiser’. This caused confusion when putting the conditional if and elif statements in the addevent_detail.html. In your template, I was using comment.organiser == user, but in my Comment model, the field that stores the user who created the comment is user, not organiser. To resolve this I replaced comment.organiser with comment.user. replaced comment.organiser  with comment.user.username to display the username of the comment. The edit button was the real issue and the change of comment.user == user so that it checks the user is the comment author.

#### URL pattern matching in urls.py. my-events path matching addevent_detail Bug
-  The path('event/<slug:slug>/', views.addevent_detail, name='addevent_detail') is being matched before path('event/my-events/', views.my_events, name='my_events'). Django matches the URLs in order from top to bottom, so when it saw event/my-events/, it treated "my-events" as a slug and tries to look up a corresponding AddEvent object, leading to the 404 error.
  To fix the issue I placed the event/my-events/ path before the event/<slug:slug>. So the more specific patterns (event/my-events) should come before less specific one.

#### Mixed Content bug
 - I was getting this error in the Issues section of Chrome inspect.
  Mixed Content: The page at '<URL>' was loaded over HTTPS, but requested an insecure element '<URL>'. This request was automatically upgraded to HTTPS, For more information see <URL>
  After researching and seeing a number of different articles, I found a fix on Slack. To fixed the mixed content i did the following. In settings.py file 
  ensure cloudinary uses https paths
  import cloudinary
  cloudinary.config(secure=True,)
  Thanks to tim_mentor for the code.

#### Summernote w3 validator error for <p> tag bug
-  Error: No p element in scope but a p end tag seen. Django Summernote.
  tim_mentor regarding issue
  It's a known bug that it adds extra paragraph tags to the body content in your posts. I think the same for the placeholders error?
  I’m aware of the issue/bug coming from Django Summernote.

#### My_events tab not Active when selected bug
-  I had added the my_events tab later then the other tabs in the nav as this was a could have in my list. I had added the link, DTL in the 'li' in the nav and the links worked bu the tab didn’t stay active. The issue was that the my_events_url was not defined in the base.html template using {% url ‘my_events” as my_events_url %}. Once I did this, it worked as expected.

#### FullCalendar and Django bug:
-  FullCalendar and Django are expecting different values for times. To resolve this a function was added to AddEventForm so the seconds are rounded down and both the front end and the backend receive the required information. 

#### FullCalendar Displaying all events and not just Published ones bug:
-  The views get_events collected all the events .all(). so it included the draft events that were not published by the admin. I needed to filter this my using the .filter(status=1) so only the status=1(Published) events are selected.

<hr>

## Future Features:
<a name="future-features"></a>
There is a number of additions that could be made to the app to increase it’s potential and appeal to users. 

- ### Develop the My_Events page to be more a profile page with more features:
  Currently the page shows the events created by the user/organiser. An added feature would be for a devision in this page. I column for created event  and a separate one for the events they’ve shown interest in, reserved seats for, shared events etc

- ### Reserve tickets:
  Similar to restaurant booking app, registers users could reserve a table or seat for an event. This feature would work well with most events, like workshops, seats at a concert etc

- ### Search bar:
  Add a search bar in the navigation menu to allow users to search for events using key words, some examples would be a venue name, a sub category, or event organiser. The search for organiser would be useful as they could be a venue that would have a number of events each week. This functionality not only saves time but also increases the likelihood of user satisfaction and retention.

- ### Sharing icon:
  Social Sharing & Friend Invites: Let users see what events their friends are attending and invite friends to join events, boosting community engagement.

- ### Favorites/Wish List: 
  Enable users to mark events as “favourites” or add them to a wish list. The user will be able to track these events on a personal page

- ### User Convenience: 
  Users can visually browse events based on proximity to their location.

- ### Event Reminders: 
  Reminders and calendar integration to help users remember to attend events they’ve indicated attendance.

- ### Share user comments: 
  As well as the share events, users can share their comments relation to an event.

- ### Event Reviews and Ratings:
  Allow attendees to leave a review and rating for the past event


## Deployment
<a name="deployment"></a>
### Heroku Deployment
This site was deployed to and is currently [hosted on the Heroku platform](https://astroshare-blog-6a7ca9d34749.herokuapp.com/). The steps for deploying to Heroku, using PostgreSQL as the database host, are as follows:

1. Create a list of requirements in the requirements.txt file by using the command pip3 freeze > requirements.txt
2. Log in (or sign up) to Heroku
3. Click on the New button and select *Create new app*
4. Give it a unique name and choose the region *Europe*
5. Click the Settings tab, go to the *Config Vars* section and click on the Reveal Config Vars button
6. Add all variables from *env.py* to ConfigVars of Heroku

<details><summary><b>Click to view details Config Vars Heroku</b></summary>

![Config vars](static/readme-img/code/Config-Vars.png)
</details>

7. Click the *Add* button
8. Click the *Deploy* tab, go to the *Deployment method section*, select *GitHub* and confirm this selection by clicking on the *Connect to Github* button
9. Search for the repository name on github *Astro Blog* and click the *Connect* button
10. Add in the *setting.py* the Heroku app URL into ALLOWED HOSTS
11. Gather all static files of the project by using the command *python3 manage.py collectstatic* in the terminal
12. Make sure that DEBUG=FALSE in *settings.py*
13. Create a *Procfile* in the root directory and add *web: gunicorn astroshare-blog.wsgi*
14. In Heroku enable the automatic deploy or manually deploy the code from the main branch

### Local Deployment
1. Generate an *env.py* file in the root directory of the project
2. Configure the environment variables within this file
3. Create a virtual environment
4. Install all required dependencies using pip install command into the .venv
5. Add dependencies to the requirements.txt file using pip3 freeze > requirements.txt command

### Final Deployment

1. Make sure to set DEBUG = False.


## Credits
<a name="credits"></a>

#### Resources Used
- Code Institute walkthrough videos in modules 'Hello Django' and 'I think therefore I blog'

- Django 5 by example, Antonio Melé

- [Pictures](https://www.purecork.ie/whats-on)
- [event pictures](https://www.corkoperahouse.ie/) 
- [band picture](https://cosmopolite.no/en/program/cosmopolite/2024/september/orchestra-baobab)

- [Center Align Navbar video](https://www.youtube.com/watch?v=1quNxUhmZNQ)
- [Stackoverflow bootstrap navbar](https://stackoverflow.com/questions/20024463/bootstrap-3-how-do-i-place-the-brand-in-the-center-of-the-navbar)
- [Stackoverflow:](https://stackoverflow.com/questions/19733447/bootstrap-navbar-with-left-center-or-right-aligned-items)
- [Django Documentation Making queries:](https://docs.djangoproject.com/en/5.1/topics/db/queries/)
- [Django filter Documentation Getting started:](https://django-filter.readthedocs.io/en/stable/guide/usage.html)
- [Django QuerySet](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#exclude)
- [Django Aggregation](https://docs.djangoproject.com/en/1.10/topics/db/aggregation/#generating-aggregates-for-each-item-in-a-queryset)
- [Model instance reference in Django](https://docs.djangoproject.com/en/5.1/ref/models/instances/)
- [Django request and response](https://docs.djangoproject.com/en/5.1/ref/request-response/#module-django.http)
- [Django request.FILES](https://stackoverflow.com/questions/3111779/how-can-i-get-the-file-name-from-request-files)
- [Django .get_or_create()](https://stackoverflow.com/questions/1941212/how-to-use-get-or-create-in-django)
- [Bootstrap Nav:](https://getbootstrap.com/docs/4.0/components/navs/)
- [Bootstrap Nav Customisation](https://stackoverflow.com/questions/61396714/i-cant-change-the-font-size-or-family-in-my-bootstrap-4-navbar)
- [Bootstrap Footer](https://getbootstrap.com/docs/5.2/examples/footers/)
- [Bootstrap borders:](https://getbootstrap.com/docs/4.0/utilities/borders/)
- [Bootstrap Spacing](https://getbootstrap.com/docs/4.0/utilities/spacing/d)
- [Bootstrap pagination](https://getbootstrap.com/docs/4.0/components/pagination/)
- [CSS borders:](https://www.w3schools.com/css/css3_borders.asp)
- [FullCalender Getting started:](https://fullcalendar.io/docs/getting-started)
- [Django QuerySet:](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#first)
- [Django Built-in class-based generic views](https://docs.djangoproject.com/fr/2.2/topics/class-based-views/generic-display/)
- [Google Font](https://fonts.google.com/selection/embed)
- [favicon.io](https://favicon.io/favicon-generator/)
- [blog.hubspot for entering an image with HTML and CSS](https://blog.hubspot.com/website/center-an-image-in-html#:~:text=Inside%20the%20curly%20brackets%2C%20I,container%20to%20a%20proportionate%20height.)
- [Center image in a div freeCodeCamp](https://www.freecodecamp.org/news/how-to-center-an-image-in-a-div-css/)
- [Bootstrap close-button](https://getbootstrap.com/docs/5.0/components/close-button/)
- [Sorting events by date vintasoftware](https://www.vintasoftware.com/blog/advanced-django-querying-sorting-events-date)
- [Django Conditional Expressions in Queries](https://micropyramid.com/blog/django-conditional-expression-in-queries)
- [Difference between the__lte and __gte in Django stack overflow](https://stackoverflow.com/questions/64309821/difference-between-the-lte-and-gte-in-django)
- [Python slugify](https://pypi.org/project/python-slugify/)
- [Bootstrap hover customisation](https://stackoverflow.com/questions/25923623/change-hover-color-on-a-button-with-bootstrap-customization)
- [Bootstrap flex](https://getbootstrap.com/docs/4.0/utilities/flex/)
- [Bootstrap remove margin under <p>](https://stackoverflow.com/questions/67309695/how-to-remove-the-margins-added-by-bootstrap)
- [Centering element css bootstrap](https://stackoverflow.com/questions/42388989/bootstrap-centering-elements-vertically-and-horizontally)
- [Django filter date and time](https://stackoverflow.com/questions/1317714/how-can-i-filter-a-date-of-a-datetimefield-in-django)
- [Django user auth for edit and delete](https://stackoverflow.com/questions/40506827/django-how-to-allow-only-the-owner-of-a-new-post-to-edit-or-delete-the-post)
- [Django calendar options](https://www.reddit.com/r/django/comments/1dowgs1/django_calendar_options/)
- [Vanilla Calendar research](https://vanilla-calendar.pro/docs/learn/getting-started/installation)
- [CSS semi transparent background](https://stackoverflow.com/questions/4790563/how-do-i-make-a-semi-transparent-background)
- [Markdown checkbox ](https://stackoverflow.com/questions/47344571/how-to-draw-checkbox-or-tick-mark-in-github-markdown-table)
- [404 Page setup for Django](https://www.youtube.com/watch?v=06Ae9FVnEOI)
- [Confirm Delete modal Youtube](https://www.youtube.com/watch?v=cufh9cOs-A4)
- [Confirm Delete](https://www.youtube.com/watch?v=3RPGYPKeXFo)
- [enctype=“multipart/form-data for image POST](https://www.w3schools.com/tags/att_form_enctype.asp)
- [enctype=“multipart/form-data](https://www.geeksforgeeks.org/what-does-enctypemultipart-form-data-mean-in-an-html-form/)
