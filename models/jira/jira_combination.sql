orders as (

    select * from {{ ref('test') }}
),

test as (
    select * from {{source('summit','new_view')}}
)

final as (
    select * from test
    UNION ALL
    select * from orders
)

select * from final