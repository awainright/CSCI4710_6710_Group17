if( JSON.parse(localStorage.getItem("list")) == null){
   var list = new Array();
}else{
    var list = JSON.parse(localStorage.getItem("list"));
   
}

var num_vampire;
var num_humans;


    function random(){
        var num = Math.floor(Math.random() * 101);
        if (num < 50){
           
            return true;
        }
        else{
            
            return false;}
    }
    
    function threshold(garlic,shadow,pale){
        
        var thresh = 0;
        if(shadow){
            thresh += 4;
        }if(garlic){
            thresh += 3;
        }if(pale){
            thresh += 3;
        }if(thresh > 6){
            
            return true;
        }
         else{
          
            return false;
        }
        
        
    }
   

    function addClassmate(fname,lname,g,s,p,ind,o){
        var form = document.getElementById('adding');
        var fName = fname;
        var lName = lname;
        var garlic = g;
        var shadow = s;
        var pale = p;
        var vampire = false;
        var x = ind;
        var y = o;
        
        if(y[x].text == "Threshold Based Method"){
            vampire = threshold(garlic,shadow,pale);
           
        }else{
            vampire = random();
           
        }
        var person = {firstname: fName, lastname: lName, noGarlic: garlic, noShadow: shadow, isPale: pale, isVampire: vampire };
        list.push(person);
        localStorage.setItem("list", JSON.stringify(list));
        addToTable(person);
        form.reset();
        
    
        
    }
   
    function count(){
        
        var userList = JSON.parse(localStorage.getItem("list")); // Retrieving
        var vamps = 0;
        var human = 0;
        for(var i = 0; i <= userList.length -1 ; i++){
            if(userList[i].isVampire){
                vamps++;
            }else{human++;}
        }
        num_humans = human;
        num_vampire = vamps;
        
        
    }


    //Load the Visualization API and the corechart package
		google.charts.load('current', {'packages':['corechart']});

		//Set a callback to run when the Google Visualization API is loaded
		google.charts.setOnLoadCallback(drawChart); 

		var chart;
		var data;
		var options;
        

		//TODO: loop for getting the number from list for humans and vampire
		

		function drawChart() {
            count();

			// Create the data table
			data = new google.visualization.DataTable();
			data.addColumn('string', 'Element');
			data.addColumn('number', 'Number');
			data.addRows([
				['Human', num_humans],
				['Vampire', num_vampire]
			]);

			//Set chart options
			options = {'title': 'How many vampires in the class',
									'width': 400,
									'height': 300};

			chart = new google.visualization.PieChart(document.getElementById('chart_div'));
            
			chart.draw(data, options);
           

		}

//This doeasnt work... I dont think we need it though.


function populateTable() {
        var table = document.getElementById("users");
        var users = JSON.parse(localStorage.getItem("list")); // Retrieving
        if(users == null){
            return;
        }else{
            //TABLE ROWS
            for (i = 0; i < users.length; i++) {
                
			    var row = table.insertRow(i +1);
                var cell1 = row.insertCell(0);
                cell1.innerHTML = users[i].firstname;
                
                var cell2 = row.insertCell(1);
                cell2.innerHTML = users[i].lastname;
              
                var cell3 = row.insertCell(2);
                cell3.innerHTML = users[i].noGarlic;
            
                var cell4 = row.insertCell(3);
                cell4.innerHTML = users[i].noShadow;
               
                var cell5 = row.insertCell(4);
                cell5.innerHTML = users[i].isPale;
        
                var cell6 = row.insertCell(5);
                cell6.innerHTML = users[i].isVampire;
                
           
                
            }
        }

            


        }

function addToTable(newPerson){
    var table = document.getElementById("users");
    var index = table.rows.length;
    var row = table.insertRow(index);
    var cell1 = row.insertCell(0);
    cell1.innerHTML = newPerson.firstname;
                
    var cell2 = row.insertCell(1);
    cell2.innerHTML = newPerson.lastname;
              
    var cell3 = row.insertCell(2);
    cell3.innerHTML = newPerson.noGarlic;
            
    var cell4 = row.insertCell(3);
    cell4.innerHTML = newPerson.noShadow;
               
    var cell5 = row.insertCell(4);
    cell5.innerHTML = newPerson.isPale;
        
    var cell6 = row.insertCell(5);
    cell6.innerHTML = newPerson.isVampire;
                
}