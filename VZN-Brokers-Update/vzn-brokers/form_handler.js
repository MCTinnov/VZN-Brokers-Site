function handleFormSubmit(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());
    
    const emailBody = `
New Lead from VZN Brokers Website!

Name: ${data.name}
Email: ${data.email}
Phone: ${data.phone}
Company: ${data.company}
Monthly Revenue: ${data.revenue}
    `.trim();
    
    // Send email via mailto (fallback)
    window.location.href = `mailto:nomasemail556@gmail.com?subject=New VZN Brokers Lead - ${data.name}&body=${encodeURIComponent(emailBody)}`;
    
    alert('Thank you! We will contact you shortly.');
    form.reset();
}
