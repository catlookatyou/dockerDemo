FROM php:7.3-fpm
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN curl -sL https://deb.nodesource.com/setup_12.x
RUN apt-get update && apt-get install -y nodejs npm vim git curl zip unzip redis-tools
RUN apt-get install libzip-dev -y
RUN docker-php-ext-configure zip --with-libzip \
    && docker-php-ext-install zip
RUN docker-php-ext-install pdo_mysql mbstring
RUN docker-php-ext-enable pdo_mysql mbstring
