(function () {
    angular.module('happyApp', ['ngRoute', 'ngMaterial']);
    angular.module('happyApp').config(function($routeProvider){
        $routeProvider
                .when('/',{
                    controller: 'CustomerController',
                    templateUrl: 'static/js/app/views/user_list.html'
                 })
                .when('/register/',{
                    controller: 'CustomerController',
                    templateUrl: 'static/js/app/views/register.html'
                 })
                .when('/list/',{
                    controller: 'CustomerController',
                    templateUrl: 'static/js/app/views/user_list.html'
                 })
                 .when('/showuser/:id',{
                    controller: 'CustomerDetailController',
                    templateUrl: 'static/js/app/views/user_view.html'
                 })
                .when('/edituser/:id',{
                    controller: 'CustomerEditController',
                    templateUrl: 'static/js/app/views/user_edit.html'
                 })
                .otherwise({redirectTo: '/' });
        });

    angular.module('happyApp').run(run);
	run.$inject = ['$http'];
	
	function run($http) {
	  $http.defaults.xsrfHeaderName = 'X-CSRFToken';
	  $http.defaults.xsrfCookieName = 'csrftoken';
	}

}());