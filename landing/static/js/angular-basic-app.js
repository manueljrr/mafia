
(function (){

    'use strict';

    var app = angular.module('mafia', []);

    app.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{/');
        $interpolateProvider.endSymbol('/}');
    });

    app.config(function($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    });

    app.controller('MemberListController', ['$http', '$log', function($http, $log) {

        var members = [];

        this.getAllMembers = function() {
            var self = this;

            showLoading();
            $http.get('/api/v1/lista-completa/').
            success(function(data, status, headers, config) {
                self.members = (data.length > 0 && data.length !== undefined) ? data : [];
                hideLoading();
            }).
            error(function(data, status, headers, config) {
                $log.error(data);
                $log.error(status);
                $log.error(headers);
                $log.error(config);
                hideLoading();
            });
        };

    }]);

    app.controller('MemberController', ['$http', '$log', function($http, $log) {
        var self = this;

        var members = [];

        this.member = {};


        this.urlConfirm = null;

        this.serverErrors = false;

        this.getAllMembers = function() {
            var self = this;

            showLoading();
            $http.get('/api/v1/lista-completa/').
            success(function(data, status, headers, config) {
                self.members = (data.length > 0 && data.length !== undefined) ? data : [];
                hideLoading();
            }).
            error(function(data, status, headers, config) {
                $log.error(data);
                $log.error(status);
                $log.error(headers);
                $log.error(config);
                hideLoading();
            });
        };

        this.reset = function() {
            this.member = {};
            this.memberForm.$setPristine();
        };

        this.register = function() {
            showLoading();
            $http.post('/api/v1/miembro/nuevo/', self.member).
                success(function(data, status, headers, config) {
                    if ( data!=undefined || data!=null ) {
                        window.location.href = self.urlConfirm + data.id;
                    }
                    hideLoading();
                }).
                error(function(data, status, headers, config) {

                    self.serverErrors = true;

                    if ( status == 500 ) {

                        $('#server-errors').html("Lo sentimos, se ha producido un error desconocido. Vuelve a intentarlo en unos segundos.");

                    } else {

                        var error = '';
                        for ( var field in data ) {
                            error += "<div>"
                            if ( ['non_field_errors', 'event'].indexOf(field) < 0 ) {
                                error += "<span class=\"error-"+ field +"\">"+ field +":</span> ";
                            }
                            error += data[field] + "</div>";
                        }
                        $('#server-errors').html(error);

                    }

                    hideLoading();
                });

        }

    }]);




    app.directive('ngMatchField', function () {
        return {
            require: 'ngModel',
            link: function (scope, iElement, iAttrs, ngModelCtrl) {
                var updateValidity = function () {
                    var viewValue = ngModelCtrl.$viewValue;
                    var isValid = isFieldValid();
                    ngModelCtrl.$setValidity('match', isValid);
                    return isValid ? viewValue : undefined;
                };

                // Test the confirm field view value matches the confirm against value.
                var isFieldValid = function () {
                    return ngModelCtrl.$viewValue === matchValue();
                };

                function matchValue() {
                    return scope.$eval(iAttrs.matchWith);
                }

                // Convert data from view format to model format
                ngModelCtrl.$parsers.push(updateValidity);

                // Watch for changes in the confirmAgainst model.
                scope.$watch('match-with', updateValidity);
                scope.$watch(function () {
                    return matchValue();
                }, updateValidity);
            }
        };
    });

    app.directive('ngMatchWith', [function () {
        return {
            require: 'ngModel',
            link: function (scope, elem, attrs, ctrl) {
                elem.on('change', function () {
                    scope.$apply(function () {
                        var v = elem.val()===document.getElementById(attrs.ngMatchWith).value;
                        ctrl.$setValidity('match', v);
                    });
                });
            }
        }
    }]);

    app.directive('ngMaterializeSelect', [function () {
        return {
            require: 'ngModel',
            link: function (scope, elem, attrs, ctrl) {
                scope.$watch(function() {
                    return elem.val();
                }, function() {
                    $('form select').material_select();
                });
            }
        }
    }]);


})();
