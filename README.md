![Visitors](https://visitor-badge.laobi.icu/badge?page_id=ramiboutas.coverletters.visitor-badge)

[![coverletters.online](https://img.shields.io/website-up-down-green-red/https/perso.crans.org.svg)](https://coverletters.online)


### :information_desk_person: What is this?

This a django web app to create multiple cover letters using #hashtag fields in the fields that change in every job application.

### :pencil: Example

:point_right: Imagine you write something like this:
~~~
Dear #recruiter,
I am a passionate django developer interested in your job application as #job_position...
[...]
~~~
:point_right: And you fill out the table as follows:

| Application | #recruiter | #job_position             |
|-------------|------------|---------------------------|
| 1           | John Doe   | Senior Backend Developer   |
| 2           | Elon Musk  | Rocket & Backend engineer |
| 3           | Manolo     | Fullstack Developer       |

Once you select your template, you will get 3 pdf files with this content :open_file_folder:

1_Application_John_Doe/coverletter.pdf :page_facing_up:
~~~
Dear John Doe,
I am a passionate django developer interested in your job application as Senior Backend Developer...
[...]
~~~

2_Application_Elon_Musk/coverletter.pdf :page_facing_up:
~~~
Dear Elon Musk,
I am a passionate django developer interested in your job application as Rocket & Backend engineer...
[...]
~~~

3_Application_Manolo/coverletter.pdf :page_facing_up:
~~~
Dear Manolo,
I am a passionate django developer interested in your job application as Fullstack Developer...
[...]
~~~

### :arrow_forward: How can I start?

Create your coverletters here: [https://coverletters.online/coverletters/new/](https://coverletters.online/coverletters/new/)

### :scroll: How it works?

1. Introduce your data: name, phone, email...
2. Modify the content of the cover letter (do not change the #hashtag fields)
3. Fill out the table for all the jobs you want to apply (the #hashtag fields will be replaced with the values of the table)
4. Select a template to generate your cover letters.
5. Download the zip file
