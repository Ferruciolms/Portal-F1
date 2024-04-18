jQuery('.data_inicio_picker').datepicker({
    format: 'dd-mm-yyyy',
    endDate: '0d',
    orientation: 'bottom',
    todayHighlight: true,
    autoclose: true,
    language: "pt-BR"
}).on("changeDate",function (e) {
    jQuery('.data_final_picker').datepicker("setStartDate", e.date);
});

var d = new Date();
var now = new Date(d.getFullYear(), d.getMonth(), d.getDate());
$('.data_inicio_picker').datepicker('update', now);


jQuery('.data_final_picker').datepicker({
    format: 'dd-mm-yyyy',
    endDate: '0d',
    autoclose: true,
    orientation: 'bottom',
    todayHighlight: true,
    language: "pt-BR",
}).on("changeDate",function (e) {
   jQuery('.data_inicio_picker').datepicker("setEndDate", e.date);
});
$('.data_final_picker').datepicker('update', now);

