/**
 * Toggle the Answer options based on question type.
 */
(function($) {
  $(function() {
    const objQT = $('#id_question_type'),
      objSASet = $('.subjective-answer'),
      objQCSet = $('#questionchoice_set-group');
    // show/hide on change
    objQT.change(function() {
      let selectedQT = $('#id_question_type option:selected').text();

      if (selectedQT == 'Objective') {
        objSASet.hide();
        objQCSet.show();
      }

      if (selectedQT == 'Subjective') {
        objSASet.show();
        objQCSet.hide();
      }
    });
    // First loading the page hide the MCQ
    objQCSet.hide();
  });
})(django.jQuery);