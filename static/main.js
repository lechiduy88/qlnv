const delete_employee = (employee_id) =>{
    fetch("/delete", {
        method: "POST",
        body: JSON.stringify({employee_id:  employee_id}),
    }).then((response) => {
        window.location.href = "/";
    })
}