function TeamCard(team: any) {
    return (
        <div>
            <div className="flex justify-center items-center relative overflow-hidden bg-cover bg-no-repeat">
                <img
                    className="rounded-t-lg"
                    src={team.data.team_logo}
                    alt="Team Logo" />
            </div>
            <div className="flex p-6 justify-center items-center">
                <h1 className="text-black font-mono">
                    {team.data.team_name}
                </h1>
            </div>
        </div>
    )
}

export default TeamCard;