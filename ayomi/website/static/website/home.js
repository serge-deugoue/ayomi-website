var email = $("#email-value").text();
var firstName = $("#firstName-value").text();
var lastName = $("#lastName-value").text();
const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

initialiseForm();

$("#change-user-data-form").on("submit", function (event) {
  event.preventDefault();
  createPost();
});
$("#cancel").on("click", function (event) {
  // reset the form
  initialiseForm();
  $("#modalUserInfo").modal("hide");
});

function createPost() {
  $.ajax({
    url: "users/change_user_info",
    type: "POST",
    headers: { "X-CSRFToken": csrftoken },
    data: {
      email: $("#form-email").val(),
      firstName: $("#form-firstName").val(),
      lastName: $("#form-lastName").val(),
    },

    // handle a successful response
    success: function (json) {
      retreiveFormValues();
      setNewValues();
      initialiseForm();
      $("#modalUserInfo").modal("hide");
    },

    // handle a non-successful response
    error: function (xhr, errmsg, err) {
      // reset the form
      initialiseForm();
      $("#modalUserInfo").modal("hide");
    },
  });
}

function initialiseForm() {
  $("#form-email").val(email);
  $("#form-firstName").val(firstName);
  $("#form-lastName").val(lastName);
}

function retreiveFormValues() {
  email = $("#form-email").val();
  firstName = $("#form-firstName").val();
  lastName = $("#form-lastName").val();
}

function setNewValues() {
  $("#email-value").text(email);
  $("#firstName-value").text(firstName);
  $("#lastName-value").text(lastName);
  $("#welcome").text("Bienvenue " + firstName + ", " + lastName);
}
