function TeamModal(props: any) {
    return (
        <>
        <div className="justify-center items-center flex overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none">
            <div className="w-full my-6 mx-auto max-w-3xl">
                <div className="border-0 rounded-lg shadow-lg flex flex-col w-full bg-white outline-none focus:outline-none">
                    <div className="flex items-center justify-between p-5 border-b border-solid border-blueGray-200 rounded-t">
                        <div className="flex items-center overflow-hidden bg-cover bg-no-repeat">
                            <img className="rounded-t-lg pr-14" src={props.data.team_logo} alt="Team Logo" />
                            <h3 className="text-black font-mono text-2xl">
                                {props.data.team_name}
                            </h3>
                        </div>
                        <button className="" onClick={() => props.stateChanger(false)}>
                            <span className="text-2xl font-mono">
                            X
                            </span>
                        </button>
                    </div>
                    <div className="relative p-6 flex-auto">
                        <p className="my-2 text-blueGray-500 font-mono text-lg leading-relaxed">
                            Position: {props.data.rank} in {props.data.conf}
                        </p>
                        <p className="my-2 text-blueGray-500 font-mono text-lg leading-relaxed">
                            Record: {props.data.wins}-{props.data.ties}-{props.data.losses} 
                        </p>
                        <p className="my-2 text-blueGray-500 font-mono text-lg leading-relaxed">
                            Goals: {props.data.goals_for}, Goals Against: {props.data.goals_against}, Diff: {props.data.goals_diff}
                        </p>
                        <p className="my-2 text-blueGray-500 font-mono text-lg leading-relaxed">
                            Attendance: {props.data.attendance_per_game}
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <div className="opacity-25 fixed inset-0 z-40 bg-black"></div>
        </>
    )
}

export default TeamModal;