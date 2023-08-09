export interface PullRequestIdentifier {
  owner: string;
  repo: string;
  prNumber: number;
}

export interface PullRequestFile {
  changeType: string;
  path: string;
}