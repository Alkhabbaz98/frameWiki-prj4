DESCRIPTION

FrameWiki is a small web project designed to help users explore and document fighting game characters and their moves. Users can browse through different games, view each character’s move list, and add, edit, or delete moves. This project serves as a simple database-driven wiki that keeps track of move data such as damage values and other properties.

Attributions

The following resources were used as external references while building the project:

Django Documentation

W3Schools

MDN Web Docs

PostgreSQL Documentation

Project's Technological Content

The main technology used in this project is Django, a Python-based web framework. Django was used to build the backend, define the models for Game, Character, and Move, and manage all CRUD (Create, Read, Update, Delete) operations for moves.

PostgreSQL was used as the database to store all data related to games, characters, and moves. Queries can be run and tested using pgAdmin.

HTML templates were used to build the structure of the web pages. Django’s template system allowed for dynamic content, such as rendering a character’s move list or showing forms to create and edit moves.

CSS was used to add styling and improve the appearance of the pages. It provided layout control and visual formatting for the forms, lists, and navigation.

Improvements for The Future

FrameWiki can be improved in many ways, including:

Adding user accounts with permissions to only allow certain users to add or edit moves.

Implementing search and filter features to find specific moves quickly.

Adding support for more move attributes like frame data, guard type, and hit level.

Improving the UI/UX with more styling and a responsive layout.

Allowing image or video attachments for moves.
