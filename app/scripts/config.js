/*global define */
define([''], function () {
    'use strict';

    var config = {};

    config.getRootUrl = function() {
        //return 'http://udacity-conf.appspot.com';
        //return 'http://localhost:8080'
        return 'http://localhost:9000'
        //return 'http://info-311.appspot.com'
        //return 'http://install-metro.appspot.com'
    }

    return config;
});