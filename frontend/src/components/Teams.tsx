import { useEffect, useState } from "react";
import TeamCard from "./TeamCard";
import TeamModal from "./TeamModal";

function Teams() {
    const [easternTeams, setEasternTeams] = useState([])
    const [westernTeams, setWesternTeams] = useState([])
    const [showModal, setShowModal] = useState(false);
    const [teamModal, setTeamModal] = useState([])

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
            <div className="flex-col mr-16">
                <h1 className="text-black font-mono m-10 text-2xl">Eastern Conference</h1>
                <div className="grid grid-cols-3">
                    {easternTeams.map((team: any, index: any) => (
                        <div key={index} onClick={() => { setShowModal(true); setTeamModal(team)}} className="block max-w-[18rem] rounded-lg bg-white text-surface shadow-secondary-1 dark:bg-surface-dark dark:text-white">
                            <TeamCard data={team} />
                        </div>
                    ))}
                </div>
            </div>
            <div className="flex-col ml-16">
                <h1 className="text-black font-mono m-10 text-2xl">Western Conference</h1>
                <div className="grid grid-cols-3">
                    {westernTeams.map((team: any, index: any) => (
                        <div key={index} onClick={() => { setShowModal(true); setTeamModal(team)}} className="block max-w-[18rem] rounded-lg bg-white text-surface shadow-secondary-1 dark:bg-surface-dark dark:text-white">
                            <TeamCard data={team} />
                        </div>
                    ))}
                </div>
            </div>

            {showModal ? (
                <>
                    <TeamModal data={teamModal}/>
                </>
            ) : null}

        </div>
    )
}

export default Teams;