Fridge Django
=======

[![GitHub issue last update](https://img.shields.io/badge/updated-may%202021-red.svg?longCache=true&style=for-the-badge)](https://github.com/logiflo/fridge-django)

# Index

- [About](#about)
- [What's New?](#whats-new)
- [How to Build](#how-to-build)
- [Requirements](#requirements)
- [Dependencies](#dependencies)
- [Demos](#demos)
- [Future features](#future)
- [Contributing](#contributing)
- [Bugs?](#bugs)
- [Honorable mentions?](#mentions)
- [License](#license)

<a name="about"></a>
# Fridge Django 1.0.1

Fridge app is an open source application using django, which allows you to keep track of the groceries you have in the fridge as well as the ones that have run out.

This application is hosted in Heroku, it is available [here](https://fridge-django.herokuapp.com/).

Version: 1.0.1 - Released: 29th May 2021

<a name="whats-new"></a>
## What's new in 1.0.1?

* The issue removing essential groceries is fixed.

<a name="how-to-build"></a>
## How to Build

Once the repo is cloned, it is required to create a file named `.env` at `fridge`. That file must contain the **SECRET_KEY** and **DATABASE_URL**; an example can be shown below:

```
SECRET_KEY=j6)1zc)bx230q^!9!@9wmfz6x!+d695iphyx%y-$tf5uf-f7b!
DATABASE_URL=sqlite:///db.sqlite3
```

Install the needed packages according to the configuration file `requirements.txt`.

```bash
$ pip install -r requirements.txt
```

Then, create a migration to create the database tables for the models defined in the application, using the following command:

```bash
$ python manage.py migrate
```

Finally, the following command starts a lightweight development Web server on the local machine. By default, the server runs on port 8000 on the IP address 127.0.0.1. You can pass in an IP address and port number explicitly.

```bash
$ python manage.py runserver
```

<a name="requirements"></a>
## Requirements

- Python 3.6 or above.

<a name="dependencies"></a>
## Dependencies

See `requirements.txt`.

<a name="future"></a>
## Future features

Coming soon...

<a name="contributing"></a>
## Contributing

- If you find a bug then please report it on [GitHub Issues][issues].

- If you have a feature request, or have written a game or demo that shows fridge-django in use, then please get in touch. We'd love to hear from you!

- If you issue a Pull Request for fridge-django, please only do so against the `dev` branch and **not** against the `master` branch.

<a name="bugs"></a>
## Bugs

Please add them to the [Issue Tracker][issues] with as much info as possible, especially source code demonstrating the issue.

<a name="license"></a>
## License
-----------------------------------------------------------------------

<a href="http://opensource.org/licenses/BSD-2-Clause" target="_blank">
<img align="right" width="100" height="137"
 src="https://opensource.org/files/OSI_Approved_License.png">
</a>

	BSD 2-Clause License

	Copyright (c) 2020, Lorena Gil
	All rights reserved.

	Redistribution and use in source and binary forms, with or without
	modification, are permitted provided that the following conditions are met:

	1. Redistributions of source code must retain the above copyright notice, this
		list of conditions and the following disclaimer.

	2. Redistributions in binary form must reproduce the above copyright notice,
		this list of conditions and the following disclaimer in the documentation
		and/or other materials provided with the distribution.

	THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
	AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
	IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
	DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
	FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
	DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
	SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
	CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
	OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
	OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

[issues]: https://github.com/logiflo/fridge-django/issues