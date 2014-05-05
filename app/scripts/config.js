/*global define */
define([''], function () {
    'use strict';

    var config = {};

    config.getRootUrl = function() {
        //return 'http://udacity-conf.appspot.com';
        //return 'http://localhost:8080'
        //return 'http://localhost:9000'
        //return 'http://info-311.appspot.com'
        return 'http://install-metro.appspot.com'
    }

    config.getScriptUrl = function() {
    // development
        return 'https://script.google.com/macros/s/AKfycbzaxbWvMoqfu-J1feZ8DzUuINz7YcOE-vdnsi-Ts0E/dev'
    // production
        //return 'https://script.google.com/macros/s/AKfycbzBrhF5qSespuqYeSWCe4puBe5OJv49euk93ESTWlELjuDELDM/exec'
    }

    return config;
});