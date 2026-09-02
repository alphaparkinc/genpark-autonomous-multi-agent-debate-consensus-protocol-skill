from client import AutonomousMultiAgentDebateConsensusProtocolClient

def main():
    client = AutonomousMultiAgentDebateConsensusProtocolClient()
    res = client.orchestrate_agent_debate('Should we deprecate REST in favor of gRPC for internal services?')
    print('Debate Consensus Protocol: ' + res['consensus_session_id'] + ' (Verdict: ' + res['consensus_verdict'] + ')')
    print('Agreement Score: ' + str(res['inter_agent_agreement_score_pct']) + '% | Steps: ' + str(res['resolved_action_plan_steps_count']))
    print('Transcript URL: ' + res['debate_transcript_log_url'])

if __name__ == '__main__':
    main()
