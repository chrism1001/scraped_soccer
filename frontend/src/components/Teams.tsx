import { useEffect, useState } from "react";

function Teams() {
    const [easternTeams, setEasternTeams] = useState([])
    const [westernTeams, setWesternTeams] = useState([])

    const fetchWesternTeams = async () => {
        const response = await fetch(`http://localhost:8000/get_teams_eastern`)
        const teams = await response.json()
        setEasternTeams(teams.data)
    }

    const fetchEasternTeams = async () => {
        const response = await fetch(`http://localhost:8000/get_teams_western`)
        const teams = await response.json()
        setWesternTeams(teams.data)
    }

    useEffect(() => {
        fetchEasternTeams()
        fetchWesternTeams()
    }, [])

    return (
        <div className="flex flex-row min-h-screen justify-center items-center">
            <div className="flex-col">
                <h1 className="text-black font-mono">Eastern Conference</h1>
                <div className="grid grid-cols-3">
                    {easternTeams.map((team: any, index: any) => (
                        <div key={index} className="block max-w-[18rem] rounded-lg bg-white text-surface shadow-secondary-1 dark:bg-surface-dark dark:text-white">
                            <div className="flex justify-center items-center relative overflow-hidden bg-cover bg-no-repeat">
                                <img
                                className="rounded-t-lg"
                                src={team.team_logo}
                                alt="Team Logo" />
                            </div>
                            <div className="flex p-6 justify-center items-center">
                                <h1 className="text-black font-mono">
                                    {team.team_name}
                                </h1>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
            <div className="flex-col">
                <h1 className="text-black font-mono">Western Conference</h1>
                <div className="grid grid-cols-3">
                    {westernTeams.map((team: any, index: any) => (
                        <div key={index} className="block max-w-[18rem] rounded-lg bg-white text-surface shadow-secondary-1 dark:bg-surface-dark dark:text-white">
                            <div className="flex justify-center items-center relative overflow-hidden bg-cover bg-no-repeat">
                                <img
                                className="rounded-t-lg"
                                src={team.team_logo}
                                alt="Team Logo" />
                            </div>
                            <div className="flex p-6 justify-center items-center">
                                <h1 className="text-black font-mono">
                                    {team.team_name}
                                </h1>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
}

export default Teams;