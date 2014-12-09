/**
 * Created by liuzheng on 14-12-8.
 */
function Hbase($scope, $http, ngTableParams) {
    $http({
        url: "/api/list",
        method: 'GET'
//        headers: {
//            "Authorization": Data.token()
//        },
//        data: {"uid": Data.uid()}
    }).success(function (data) {
        $scope.status = data["status"];//1 true or 0 false
        //Data.token = data["token"];
//        $scope.message = data["message"];
        $scope.data = data['data']
        if ($scope.status) {
            //仅需要对message中的数据做处理
        } else {

        }
    }).error(function (data) {

    });
}