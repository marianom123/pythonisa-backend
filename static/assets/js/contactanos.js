document.getElementById("contactForm").addEventListener("submit", function(event) {
  event.preventDefault();
  let name = document.getElementById("name");
  let last_name = document.getElementById("last_name");
  let phone = document.getElementById("phone");
  let email = document.getElementById("email");
  let subject = document.getElementById("subject");
  let message = document.getElementById("message");
  let newsletter = document.getElementById("newsletter");

  let isValid = true;

  if (name.value == "") {
      name.classList.add("error");
      isValid = false;
      alert("Por favor, ingresa tu nombre");
      setTimeout(function() {
        name.classList.remove("error");}, 2000);
  } else {
      name.classList.remove("error");
      name.classList.add("success"); 
  }

  if (last_name.value == "") {
      last_name.classList.add("error");
      isValid = false;
      alert("Por favor, ingresa tu apellido");
      setTimeout(function() {
        last_name.classList.remove("error");}, 2000);
  } else {
      last_name.classList.remove("error");
      last_name.classList.add("success"); 
  }

  if (phone.value == "") {
      phone.classList.add("error");
      isValid = false;
      alert("Por favor, ingresa tu teléfono");
      setTimeout(function() {
        phone.classList.remove("error");}, 2000);
  } else {
      phone.classList.remove("error");
      phone.classList.add("success"); 
  }

  if (email.value == "") {
      email.classList.add("error");
      isValid = false;
      alert("Por favor, ingresa tu correo");
      setTimeout(function() {
        email.classList.remove("error");}, 2000);
  } else {
      email.classList.remove("error");
      email.classList.add("success"); 
  }

  if (subject.value == "") {
      subject.classList.add("error");
      isValid = false;
      alert("Por favor, ingresa el asunto");
      setTimeout(function() {
        subject.classList.remove("error");}, 2000);
  } else {
      subject.classList.remove("error");
      subject.classList.add("success"); 
  }
      
  if (message.value == "") {
      message.classList.add("error");
      isValid = false;
      alert("Por favor, ingresa tu consulta");
      setTimeout(function() {
        message.classList.remove("error");}, 2000);
  } else {
      message.classList.remove("error");
      message.classList.add("success"); 
  }
  
  if (document.querySelector('input[name=source]:checked') == null) {
      isValid = false;
      alert("Por favor, selecciona una opción válida");
  }

  if (!newsletter.checked) {
      isValid = false;
      alert("Por favor, acepta la newsletter");
  }

  if (isValid) {
      alert("Gracias por contactarnos");
      this.reset();

      setTimeout(function() {
          name.classList.remove("success");
          last_name.classList.remove("success");
          phone.classList.remove("success");
          email.classList.remove("success");
          subject.classList.remove("success");
          message.classList.remove("success");
      }, 2000); 
  }
});