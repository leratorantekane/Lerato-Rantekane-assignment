const seasons = [...Array(2022-2004+1)].map((_,i) => 2005+i);
const fetchSeasonData = async (season) => {
  const response = await fetch(`http://ergast.com/api/f1/${season}/drivers.json`);
  const data = await response.json();
  return data.MRData.DriverTable.Drivers;
};

const fetchAllSeasonData = async () => {
  const allSeasonData = await Promise.all(seasons.map(season => fetchSeasonData(season)));
  return allSeasonData.flat();
};

const displayData = async () => {
  const driversData = await fetchAllSeasonData();
    console.log(driversData);
    data = {
      data: driversData,
      wins: driversData[driverId]
    }
};

displayData();

// Function to retrieve driver data and display it on the page
function onDriverSelect() {
  var d = document.getElementById("driver-select");
  var driverId = d.options[d.selectedIndex].value;

  const options = {
    method: 'GET',
  };

  fetch(`http://ergast.com/api/f1/${season}/drivers/${driverId}/driverStandings.json`, options)
    .then(result => result.json())
    .then(data => {
      console.log(data);
      data = {
        data: data,
        wins: driversData[driverId]
      }

      const template = document.getElementById('driver-template').innerText;
      const compiledFunction = Handlebars.compile(template);
      document.getElementById('root').innerHTML = compiledFunction(data);
    });
};

function displayChampions() {
    var d = document.getElementById("champions");
    var driverId = d.options[d.selectedIndex].value;

    const options = {
    method: 'GET',
    };

    fetch(`http://ergast.com/api/f1/${season}/constructors/${championId}/results.json`, options)
        .then(result => result.json())
        .then(data => {
            console.log(data);
            data = {
              data: data,
              champion: driversData[championId]
    }

    const template = document.getElementById('champions-template').innerText;
    const compiledFunction = Handlebars.compile(template);
    document.getElementById('root').innerHTML = compiledFunction(data);
    });

};

function onRaceSelect() {
    var d = document.getElementById("champion-results");
    var driverId = d.options[d.selectedIndex].value;

    const options = {
      method: 'GET',
    };

    fetch(`http://ergast.com/api/f1/${season}/drivers/${driverId}/results.json`, options)
      .then(result => result.json())
      .then(data => {
        console.log(data);
        data = {
          data: data,
          winner: driversData[driverId]
        }

        const template = document.getElementById('races-template').innerText;
        const compiledFunction = Handlebars.compile(template);
        document.getElementById('root').innerHTML = compiledFunction(data);
      });
};

//Gamification to complete
 const points = 0;
 const level = 1;
 const levelUpPoints = 10;

 function updatePoints(newPoints) {
   points += newPoints;
   document.getElementById("points").innerText = `Points: ${points}`;

   if (points >= levelUpPoints) {
     level += 1;
     document.getElementById("level").innerText = `Level: ${level}`;
     levelUpPoints += level * 10;
   }
 }

 document.getElementById("increase-points").addEventListener("click", function() {
   updatePoints(1);
 });

 document.getElementById("decrease-points").addEventListener("click", function() {
   updatePoints(-1);
 });
