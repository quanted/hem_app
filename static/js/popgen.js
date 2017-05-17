

$("input[name=inlineRadioOptions]").change(function() {
  var divId = $(this).attr("id");
  $("div.pc").hide();
  $("." + divId).show();

})