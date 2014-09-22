// Generated by CoffeeScript 1.8.0
(function() {
  var $;

  $ = jQuery;

  $(document).ready(function() {
    var phraseField, phraseText;
    phraseField = $("#phrase");
    phraseText = phraseField.val();
    console.log(phraseText);
    $(".choosable").click(function() {
      var oldValue;
      oldValue = phraseField.val();
      if (oldValue !== "") {
        oldValue += " ";
      }
      return phraseField.val(oldValue + $(this).text().replace(/\s+/g, '').replace(/[\.,\/#!?$%\^&\*;:{}=\_"`~()]/g, ""));
    });
    return $("#clearphrase").click(function() {
      return phraseField.val("");
    });
  });

}).call(this);
