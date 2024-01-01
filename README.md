# Roundcube webmail plugin "rcguard"

## Introduction

This plugin logs failed login attempts and requires users to go through
a CAPTCHA verification process when the number of failed attempts go
too high. It provides protection against automated attacks.

Failed attempts are logged by IP and stored in a database table.
IPs are also released after a certain expire amount of time.

Since 2024-01-01 the default config is set to always activate CAPTCHA verification by

`$config['failed_attempts'] = 0;`

## Sources

### Repositories

- GitHub: https://github.com/pbiering/roundcube-rcguard

### Registrations

- Packagist: https://packagist.org/packages/pbiering/rcguard

## Installation

### With Composer

Add this plugin `pbiering/rcguard` to the `require` section of your Roundcube
`composer.json`, run composer update and enable rcguard in the main Roundcube
configuration file.
<br>OR just run:

    composer require pbiering/rcguard

### Manually

#### Installation

Place the contents of this directory under `plugins/rcguard`.

#### Activation

Enable rcguard in the main Roundcube configuration file (e.g. `/etc/roundcubemail/config.inc.php`)
by extension of the plugin config array:

`array_push($config['plugins'], 'rcguard');`


## Configuration

Copy `config.inc.php.dist` to `config.inc.php` and modify as necessary.

Use the files under `SQL/` to create the database schema required for
rcguard. The table should be created in the database used by Roundcube.
**NOTE**: If you use the Roundcube `db_prefix` config option, you must rename
the table `rcguard` accordingly.


### Customizing CAPTCHA

<big>**IMPORTANT: This plugin requires CAPTCHA API keys to work properly.**</big>
<br>These can be obtained from:
- Google reCAPTCHA: https://www.google.com/recaptcha
- hCaptcha: https://dashboard.hcaptcha.com/
- FriendlyCaptcha: https://friendlycaptcha.com/
- Cloudflare Turnstile: https://www.cloudflare.com/products/turnstile/

You may customize the following in the `config.inc.php` file:

- the API version: `v3`, `v2invisible`, `v2`, `v2hcaptcha` or `v2friendlycaptcha` or `v2cfturnstile`;
 by `$config['recaptcha_api_version']`
  - also configure per selected service required `$config['recaptcha_api_url']`, `$config['recaptcha_publickey']`, `$config['recaptcha_privatekey']`

- the v2 widget theme: `light` or `dark` (where supported);
 by `$config['recaptcha_theme']'

- the v2 widget size: `normal` or `compact` (where supported).
 by `$config['recaptcha_size']`

For more information about the widget please check:
- [documentation about reCAPTCHA][recaptcha-doc]
- [documentation about hCaptcha][hcaptcha-doc].
- [documentation about FriendlyCaptcha][friendlycaptcha-doc]
- [documentation about Cloudflare Turnstile][cfturnstile-doc]

The plugin configuration file has several other options you may configure, please take at look.

Since May 2018, you can define a proxy (anonymous or authenticated) to request the CAPTCHA widget.

Since April 2022, support for hCaptcha and FriendlyCaptcha was added

Since March 2023, support for Cloudflare Turnstile was added


## Supported databases

- MySQL
- PostgreSQL
- SQLite


## Contact

The original author of this plugin was [Denny Lin][dennylin].

[Diana Soares][dsoares] forked
it some years ago to 1) use reCAPTCHA v2.0, 2) add the larry skin and 3) because the project
issues were taking too long to be answered. Also, the original project was not
updated since 2015 and many things have changed in the meantime in Roundcube's API.

[Peter Bieringer][pbiering] forked it 2022 from [Diana Soares][dsoares] to add additional
Captcha services.

Because of the former fork went also stale in 2021 (https://github.com/dsoares/roundcube-rcguard/issues/50),
[Peter Bieringer][pbiering] will maintain this project now.

Comments and suggestions are welcome via "issues".

[pbiering]: https://github.com/pbiering
[dsoares]: https://github.com/dsoares
[dennylin]: https://github.com/dennylin93
[recaptcha-doc]: https://developers.google.com/recaptcha/intro
[hcaptcha-doc]: https://docs.hcaptcha.com/
[friendlycaptcha-doc]: https://docs.friendlycaptcha.com/
[cfturnstile-doc]: https://developers.cloudflare.com/turnstile/


## License

This plugin is distributed under the GPL-3.0+ license.

This plugin also contains PHP libraries for
- reCAPTCHA
- hCaptcha
- FriendlyCaptcha
- Cloudflare Turnstile

that are distributed under its own licenses. See the library files for the exact details.

