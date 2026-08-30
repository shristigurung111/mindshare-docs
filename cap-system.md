# Cap System

The cap system limits how many posts per user can contribute to their score within a specific time period. This prevents users from dominating the leaderboard simply by posting large volumes of low-quality content.

The cap logic is implemented in **CTE 6 (STEP 6: POST CAP)** of the function, specifically in the `ranked_posts` and `capped_posts` CTEs. The cap configuration is looked up from the `mindshare.project_post_cap` table in the function's declaration section, before the main SQL execution begins.

Cap rules are stored in the `mindshare.project_post_cap` table and are looked up based on the resolved leaderboard type. Each project and leaderboard type combination can have its own cap configuration.

## Cap Configuration

The cap configuration consists of three components:

| Component          | Description                                                                                                                                                                                                                                                                                          |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Post_cap**       | The maximum number of posts per user that count toward their score within each time bucket. A value of `0` means no cap (all posts count).                                                                                                                                                           |
| **Cap_period**     | The time bucket size. Possible values are `'day'`, `'week'`, `'month'`, or `'none'`. When `'none'` is used, all posts fall into a single bucket.                                                                                                                                                     |
| **Cap_start_date** | The anchor point for bucket boundaries. When set, buckets align to this timestamp. When `NULL`, it falls back to `project_start_date`. If `project_start_date` is also `NULL`, then calendar defaults are used (midnight UTC for days, Sunday 00:00 UTC for weeks, the 1st of the month for months). |

## How the Cap Works

For each combination of user and time bucket:

1. All non-reply posts are ranked by their `post_score` in descending order.
2. Only the top `post_cap` posts are kept.
3. All posts beyond the cap are discarded and contribute nothing to the user's score.

## Why the Cap Exists

Without a cap, users who post frequently (even low quality) would outrank users who post high-quality content occasionally. The cap ensures **quality matters more than quantity**, encouraging meaningful contributions rather than volume farming.

## Important Rules

- **Replies are never capped** — they always count toward the reply bonus.
- **Cap = 0 means uncapped** — all posts pass through.
- **Different leaderboard types can have different caps** — public, private, and Nucleus boards can each have their own configuration.
