document.getElementById('myForm').addEventListener('submit', saveTask);

function saveTask(e){
    var taskName = document.getElementById("taskName").value;
    var taskDescription = document.getElementById("taskDescription").value;
    var taskDate = document.getElementById("taskDate").value;
    
    var task = {
    name:taskName,
    description:taskDescription,
    date:taskDate
    }
    e.preventDefault();
    if(localStroage.getItem('tasks')==null){
        var task =[]; task.push(tasks);
        localStorage.SetItem('task',JSON.stringyfy(task));
        }
        else{
        var myTask = localStorage.getItem('task'); 
        myTask.push(task);
        // then reset the localStorage
        localStorage.setItem('task',JSON.stringify(myTask));
        }
}

function fetchTask(){
    var task = JSON.parse(localStorage.getItem('task'));

    var taskResult =  document.getElementById('taskResult');
    taskResult.innerHTML = "";

    for (let i = 0; i < task.length; i++) {
        var name   = task[i].name;
        var description = task[i].description;        
        var date = task[i].date;        

        taskResult.innerHTML+= '<div class="well"><h3>'+name+' '+description+' '+date+' </h3>'
        '</div>'
    }
}

