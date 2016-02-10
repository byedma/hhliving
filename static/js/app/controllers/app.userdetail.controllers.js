(function () {  
    function CustomerDetailController($scope,$log,$routeParams, CustomerService) {
        $scope.user  = {};

        function init(){
           CustomerService.getuser($routeParams.id)
            .success(function(user){
                $scope.user = user;
            })
            .error(function(data,status,headers,config){
                // Error Handling
                //$log.log('data:'+data+'status'+status+'headers'+headers+'config'+config);
                //alert("Error"+data+status);
            });
        }

        init();

    };
    angular.module('happyApp').controller('CustomerDetailController',CustomerDetailController);
           
}());