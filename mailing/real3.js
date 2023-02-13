const form = document.querySelector("#email-template-form");
const savedTemplatesSelect = document.querySelector("#saved-templates");
const useTemplateButton = document.querySelector("#use-template");

// An array to store the saved templates
let templates = [];

// Submit event listener for the form
form.addEventListener="submit", e => 
  e.preventDefault();

  // Get the form data
  const templateName = form.templateName.value;
  const subject = form.subject.value;
  const body = form.body.value;

  // Save the template
  templates.push({ templateName, subject, body });

  // Clear the form
  form.reset();


