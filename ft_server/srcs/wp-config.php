<?php

define('DB_NAME', 'wordpress');
define('DB_USER', 'csherril');
define('DB_PASSWORD', 'kXzqP3dDdeIpAsU');
define('DB_HOST', 'localhost');
define('DB_CHARSET', 'utf8');
define('DB_COLLATE', '');

define( 'AUTH_KEY',         'x94?IT9YxS#Q@a?X?aY7YStS5~?Twc' );
define( 'SECURE_AUTH_KEY',  '~V~c5ESQu~O$OqBR2f*7NtK0I|dXd~' );
define( 'LOGGED_IN_KEY',    'KYyHpNbNaWPnk$DJw%sjAD}3sL66bG' );
define( 'NONCE_KEY',        '|@YKg$h|fmG7|2douOdkC$xyoKlhK6' );
define( 'AUTH_SALT',        'e0BwmaS7rOgCljn|pVom~tWhEPzMJS' );
define( 'SECURE_AUTH_SALT', 'iGQCFuETs5GxvlV}0#lY@G{#JeA0uj' );
define( 'LOGGED_IN_SALT',   'FZfhWwWqP3pWHU3C{ufrgcQ%r0KAPH' );
define( 'NONCE_SALT',       'nIr2CzAOwVDvezuWG6sw%~Lj9{Eo08' );

$table_prefix = 'wp_';

define( 'WP_DEBUG', false );

if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}
require_once( ABSPATH . 'wp-settings.php' );
