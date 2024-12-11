from collections import deque

suggested_links = deque([int(x) for x in input().split()])
featured_articles = [int(x) for x in input().split()]
target_engagement_value = int(input())
final_feed = []

while suggested_links and featured_articles:
    current_link = suggested_links[0]
    current_article = featured_articles[-1]

    if current_article > current_link:
        current_result = featured_articles.pop() % suggested_links.popleft()
        final_feed.append(abs(current_result))
        if current_result != 0:
            featured_articles.append(2 * current_result)
    elif current_link > current_article:
        current_result = suggested_links.popleft() % featured_articles.pop()
        final_feed.append(abs(current_result) * -1)
        if current_result != 0:
            suggested_links.append(2 * current_result)
    else:
        featured_articles.pop()
        suggested_links.popleft()
        final_feed.append(0)

total_engagement_value = sum(final_feed)
print(f"Final Feed: {', '.join(str(x) for x in final_feed)}")
if total_engagement_value >= target_engagement_value:
    print(f"Goal achieved! Engagement Value: {total_engagement_value}")
else:
    shortfall = target_engagement_value - total_engagement_value
    print(f"Goal not achieved! Short by: {shortfall}")
