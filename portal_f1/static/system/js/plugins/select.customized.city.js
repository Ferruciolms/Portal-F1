$(document).ready(function(){
    $('.js-example-basic-single').select2({
        placeholder: "Selecione",
        width: "100%",
        allowClear: true,
        language: {
            inputTooShort: function (args) {

                return "Digite 3 caracteres";
            },
            noResults: function () {
                return "Não encontrado";
            },
            searching: function () {
                return "Procurando...";
            }
        },
        minimumInputLength: 3,
        });
});
