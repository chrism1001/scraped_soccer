import { useEffect, useState } from "react";

function Teams() {
    const [teams, setTeams] = useState([])

    const fetchTeams = async () => {
        const response = await fetch(`http://localhost:8000/get_teams`)
        const teams = await response.json()
        setTeams(teams.data)
    }

    useEffect(() => {
        fetchTeams()
    }, [])

    console.log(teams)

    return (
        <>
            <div>
                
            </div>
        </>
    )
}

export default Teams;