(function () {
    
    var CustomerService = function($http) {
         
        this.getCustomers = function(){
            return $http.get('/customers');
        };
        
        this.login = function(email, password){
            return $http.post('/api/v1/users/', 
            { 
              email: email, 
              password: password
            }).then(loginSuccessFn, loginErrorFn);
        };
        

        this.userList = function(){
            return $http.get('/api/v1/users/');
        };

        this.getuser = function(id){
            return $http.get('/api/v1/users/'+ id);
        };

        this.deleteUser = function(id){
            return $http.delete('/api/v1/users/'+ id).
            then(generalSuccessFn, generalErrorFn);
        };

        function generalSuccessFn(response) {
                window.location = '#/list';
        }

        function generalErrorFn(response) {
              alert("Could not delete");
              console.error('Epic failure!');
        }

        this.updateUserdetail = function(vm){
           return $http.put('/api/v1/edit_users/'+vm.id + '/', 
            { 
              email: vm.email,
              first_name: vm.first_name,
              middle_name: vm.middle_name,
              last_name: vm.last_name,
              title: vm.title,
              gender: vm.gender
            }).then(registerSuccessFn, registerErrorFn);
        };


        this.register = function(vm){

           return $http.post('/api/v1/users/', 
            { 
              first_name: vm.first_name,
              middle_name: vm.middle_name,
              last_name: vm.last_name,
              password: vm.password,
              confirm_password: vm.confirm_password,
              email: vm.email,
              title: vm.title,
              gender: vm.gender
            }).then(registerSuccessFn, registerErrorFn);
        };

        function registerSuccessFn(response) {
                window.location = '#/list';
        }

        function registerErrorFn(response) {
              alert(response.status);
              alert(response.data.email);
              console.error('Epic failure!');
        }

        function loginSuccessFn(response) {
                Authentication.setAuthenticatedAccount(data.data);
                window.location = '/';
        }

        function loginErrorFn(response) {
              console.error('Epic failure!');
        }

    };
    
    angular.module('happyApp').service('CustomerService',CustomerService);
           
}());