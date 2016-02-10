(function () {  
    function CustomerController($scope,$log, CustomerService) {

        $scope.users = [];

        function init(){
           
            CustomerService.userList()
            
            .success(function(users){
                $scope.users = users;
            })
            
            .error(function(data,status,headers,config){
                // Error Handling
                //$log.log('data:'+data+'status'+status+'headers'+headers+'config'+config);
                //alert("Error"+data+status);
            });
        }
        
        init();

        $scope.register = function () {
            CustomerService.register($scope.vm);
        }; 

        $scope.deleteuser = function(id) {
            CustomerService.deleteUser(id);
        };
    };
    
    angular.module('happyApp').controller('CustomerController',CustomerController);
           
}());