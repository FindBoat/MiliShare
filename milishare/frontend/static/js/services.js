'use strict';

var milishareServices = angular.module('milishareServices', ['ngResource']);

milishareServices.factory('Cards', function($resource) {
	return $resource('/api/cards');
});
