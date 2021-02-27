FROM php:7.3-fpm
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
RUN bash nodesource_setup.sh
RUN apt update && apt install -y nodejs
RUN apt install -y vim git curl zip unzip redis-tools
RUN apt install libzip-dev -y
RUN docker-php-ext-configure zip --with-libzip \
    && docker-php-ext-install zip
RUN docker-php-ext-install pdo_mysql mbstring
RUN docker-php-ext-enable pdo_mysql mbstring
