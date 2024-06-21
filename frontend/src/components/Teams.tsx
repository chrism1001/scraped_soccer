import { useEffect, useState } from "react";
import TeamCard from "./TeamCard";

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

    return (
        <div className="flex flex-row min-h-screen justify-center items-center">
            <div className="grid grid-cols-3">
                {teams.map(team => (
                    <div className="">
                        <TeamCard team={team} />
                    </div>
                ))}
            </div>
        </div>
    )
}

export default Teams;